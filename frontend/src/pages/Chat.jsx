import { useState } from "react";
import axios from "axios";
import Layout from "../components/Layout";
import { Bot, User, Send, Sparkles } from "lucide-react";

function Chat() {

    const [repoId, setRepoId] = useState("");
    const [question, setQuestion] = useState("");

    const [answer, setAnswer] = useState("");
    const [sources, setSources] = useState([]);
    const [queryType, setQueryType] = useState("");

    const [loading, setLoading] = useState(false);

    const askQuestion = async () => {

        if (!repoId || !question.trim()) {
            alert("Please enter Repository ID and Question");
            return;
        }

        try {

            setLoading(true);
            setAnswer("");
            setSources([]);
            setQueryType("");

            const response = await axios.post(
                "http://localhost:8000/chat",
                {
                    repo_id: Number(repoId),
                    question
                }
            );

            setAnswer(response.data.answer || "");
            setSources(response.data.sources || []);
            setQueryType(response.data.query_type || "");

        } catch (err) {

            console.log(err);

            setAnswer("Unable to generate response.");

        } finally {

            setLoading(false);

        }

    };

    return (

        <Layout>

            <div className="max-w-5xl">

                <h1 className="text-5xl font-bold text-amber-50 mb-3">

                    AI Repository Chat

                </h1>

                <p className="text-amber-200/70 mb-10">

                    Ask anything about your repository.

                </p>

                <div className="bg-[#2A1E17] rounded-3xl border border-amber-900/40 p-8">

                    <input
                        type="number"
                        placeholder="Repository ID"
                        value={repoId}
                        onChange={(e)=>setRepoId(e.target.value)}
                        className="w-full p-4 rounded-xl bg-[#1A120E] border border-amber-900/40 mb-5"
                    />

                    <textarea
                        rows={5}
                        value={question}
                        onChange={(e)=>setQuestion(e.target.value)}
                        placeholder="Ask your question..."
                        className="w-full p-4 rounded-xl bg-[#1A120E] border border-amber-900/40 resize-none"
                    />

                    <button
                        onClick={askQuestion}
                        disabled={loading}
                        className="mt-6 flex items-center gap-2 bg-amber-700 hover:bg-amber-600 px-6 py-3 rounded-xl"
                    >
                        <Send size={18}/>
                        {loading ? "Thinking..." : "Ask AI"}
                    </button>

                </div>

                {question && (

                    <div className="mt-10 flex justify-end">

                        <div className="bg-amber-700 rounded-3xl p-5 max-w-3xl flex gap-4">

                            <User/>

                            <div>

                                <p className="font-semibold">

                                    You

                                </p>

                                <p>

                                    {question}

                                </p>

                            </div>

                        </div>

                    </div>

                )}

                {answer && (

                    <div className="mt-8 flex">

                        <div className="bg-[#2A1E17] rounded-3xl p-6 max-w-4xl flex gap-5 border border-amber-900/40">

                            <Bot className="text-amber-400"/>

                            <div>

                                <div className="flex items-center gap-3 mb-3">

                                    <h2 className="font-bold">

                                        EEIP Assistant

                                    </h2>

                                    {

                                        queryType &&

                                        <span className="bg-amber-700 px-3 py-1 rounded-full text-sm">

                                            <Sparkles size={14} className="inline mr-1"/>

                                            {queryType}

                                        </span>

                                    }

                                </div>

                                <div className="whitespace-pre-wrap leading-8 text-amber-50/90">

                                    {answer}

                                </div>

                            </div>

                        </div>

                    </div>

                )}

                {

                    sources.length>0 &&

                    <div className="mt-10">

                        <h2 className="text-2xl font-bold mb-6">

                            Sources

                        </h2>

                        <div className="grid md:grid-cols-2 gap-5">

                            {

                                sources.map((source,index)=>(

                                    <div
                                        key={index}
                                        className="bg-[#2A1E17] rounded-2xl border border-amber-900/40 p-5"
                                    >

                                        <p>

                                            <strong>File:</strong>

                                            {" "}

                                            {source.file}

                                        </p>

                                        <p className="mt-2">

                                            <strong>Chunk:</strong>

                                            {" "}

                                            {source.chunk}

                                        </p>

                                        <p className="mt-2">

                                            <strong>Lines:</strong>

                                            {" "}

                                            {source.start_line}

                                            -

                                            {source.end_line}

                                        </p>

                                    </div>

                                ))

                            }

                        </div>

                    </div>

                }

            </div>

        </Layout>

    );

}

export default Chat;