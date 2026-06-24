import { useState } from "react";
import axios from "axios";

function Chat() {

    const [repoId, setRepoId] = useState("");
    const [question, setQuestion] = useState("");

    const [answer, setAnswer] = useState("");
    const [sources, setSources] = useState([]);
    const [queryType, setQueryType] = useState("");

    const [loading, setLoading] = useState(false);

    const askQuestion = async () => {

        if (!repoId || !question.trim()) {
            alert(
                "Please enter Repository ID and Question"
            );
            return;
        }

        try {

            setLoading(true);

            setAnswer("");
            setSources([]);
            setQueryType("");

            const response = await axios.post(
                "http://localhost:8001/chat",
                {
                    repo_id: Number(repoId),
                    question: question
                }
            );

            setAnswer(
                response.data.answer || ""
            );

            setSources(
                response.data.sources || []
            );

            setQueryType(
                response.data.query_type || ""
            );

        } catch (error) {

            console.error(error);

            setAnswer(
                "Failed to get answer from backend."
            );

        } finally {

            setLoading(false);
        }
    };

    return (
        <div
            style={{
                maxWidth: "1000px",
                margin: "40px auto",
                padding: "20px",
                fontFamily: "Arial"
            }}
        >
            <h1>Repository Chat</h1>

            <input
                type="number"
                placeholder="Repository ID"
                value={repoId}
                onChange={(e) =>
                    setRepoId(e.target.value)
                }
                style={{
                    width: "100%",
                    padding: "12px",
                    marginBottom: "15px",
                    borderRadius: "6px",
                    border: "1px solid #ccc"
                }}
            />

            <textarea
                placeholder="Ask a question..."
                value={question}
                onChange={(e) =>
                    setQuestion(e.target.value)
                }
                rows={5}
                style={{
                    width: "100%",
                    padding: "12px",
                    borderRadius: "6px",
                    border: "1px solid #ccc"
                }}
            />

            <button
                onClick={askQuestion}
                disabled={loading}
                style={{
                    marginTop: "15px",
                    padding: "12px 25px",
                    cursor: loading
                        ? "not-allowed"
                        : "pointer"
                }}
            >
                {loading
                    ? "Thinking..."
                    : "Ask"}
            </button>

            {answer && (

                <div
                    style={{
                        marginTop: "30px",
                        padding: "20px",
                        border: "1px solid #ddd",
                        borderRadius: "8px"
                    }}
                >

                    {queryType && (
                        <div
                            style={{
                                marginBottom: "20px",
                                padding: "12px",
                                backgroundColor:
                                    "#e0f2fe",
                                borderRadius: "8px"
                            }}
                        >
                            <strong>
                                Agent Used:
                            </strong>{" "}
                            {queryType}
                        </div>
                    )}

                    <h2>Answer</h2>

                    <div
                        style={{
                            whiteSpace:
                                "pre-wrap",
                            lineHeight: "1.7"
                        }}
                    >
                        {answer}
                    </div>

                    {sources.length > 0 && (
                        <>
                            <hr
                                style={{
                                    marginTop:
                                        "25px",
                                    marginBottom:
                                        "20px"
                                }}
                            />

                            <h2>Sources</h2>

                            {sources.map(
                                (
                                    source,
                                    index
                                ) => (
                                    <div
                                        key={
                                            index
                                        }
                                        style={{
                                            marginBottom:
                                                "15px",
                                            padding:
                                                "15px",
                                            backgroundColor:
                                                "#f5f5f5",
                                            borderRadius:
                                                "8px",
                                            border:
                                                "1px solid #ddd"
                                        }}
                                    >
                                        <p>
                                            <strong>
                                                File:
                                            </strong>{" "}
                                            {
                                                source.file
                                            }
                                        </p>

                                        <p>
                                            <strong>
                                                Chunk:
                                            </strong>{" "}
                                            {
                                                source.chunk
                                            }
                                        </p>

                                        <p>
                                            <strong>
                                                Lines:
                                            </strong>{" "}
                                            {
                                                source.start_line
                                            }
                                            {" - "}
                                            {
                                                source.end_line
                                            }
                                        </p>
                                    </div>
                                )
                            )}
                        </>
                    )}
                </div>
            )}
        </div>
    );
}

export default Chat;