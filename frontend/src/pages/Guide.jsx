import { useState } from "react";
import axios from "axios";
import Layout from "../components/Layout";
import { BookOpen, FileText } from "lucide-react";

function Guide() {

    const [repoId, setRepoId] = useState("");
    const [guide, setGuide] = useState("");
    const [loading, setLoading] = useState(false);

    const generateGuide = async () => {

        if (!repoId) {
            alert("Please enter Repository ID");
            return;
        }

        try {

            setLoading(true);
            setGuide("");

            const response = await axios.post(
                `http://localhost:8000/generate-guide?repo_id=${repoId}`
            );

            setGuide(response.data.guide);

        } catch (error) {

            console.error(error);

            setGuide("Failed to generate repository guide.");

        } finally {

            setLoading(false);

        }

    };

    return (

        <Layout>

            <h1 className="text-5xl font-bold text-[#f5e6d3] mb-3">
                Repository Guide
            </h1>

            <p className="text-[#c7a98d] text-xl mb-10">
                Automatically generate documentation for any repository.
            </p>

            <div className="bg-[#2a1d15] border border-[#4a3121] rounded-3xl p-8 shadow-2xl">

                <div className="flex items-center gap-3 mb-6">

                    <BookOpen
                        size={30}
                        className="text-[#c68b59]"
                    />

                    <h2 className="text-3xl font-semibold text-[#f5e6d3]">
                        Repository Guide Generator
                    </h2>

                </div>

                <input
                    type="number"
                    placeholder="Repository ID"
                    value={repoId}
                    onChange={(e)=>setRepoId(e.target.value)}
                    className="
                        w-full
                        bg-[#1d140f]
                        border
                        border-[#4a3121]
                        rounded-xl
                        px-5
                        py-4
                        text-white
                        mb-6
                        focus:outline-none
                        focus:border-[#c68b59]
                    "
                />

                <button
                    onClick={generateGuide}
                    disabled={loading}
                    className="
                        bg-[#c66b18]
                        hover:bg-[#da7b24]
                        text-white
                        px-8
                        py-4
                        rounded-xl
                        font-semibold
                        transition-all
                    "
                >
                    {loading ? "Generating..." : "Generate Guide"}
                </button>

            </div>

            {guide && (

                <div className="bg-[#2a1d15] border border-[#4a3121] rounded-3xl p-8 shadow-2xl mt-10">

                    <div className="flex items-center gap-3 mb-6">

                        <FileText
                            size={28}
                            className="text-[#c68b59]"
                        />

                        <h2 className="text-3xl font-semibold text-[#f5e6d3]">
                            Repository Guide
                        </h2>

                    </div>

                    <pre
                        className="
                            whitespace-pre-wrap
                            break-words
                            leading-8
                            text-[#d9c5b2]
                            text-base
                            font-mono
                            bg-[#1d140f]
                            border
                            border-[#4a3121]
                            rounded-xl
                            p-6
                            overflow-x-auto
                        "
                    >
                        {guide}
                    </pre>

                </div>

            )}

        </Layout>

    );

}

export default Guide;