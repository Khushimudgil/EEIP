import { useState } from "react";
import axios from "axios";
import Layout from "../components/Layout";
import { Network } from "lucide-react";

function KnowledgeGraph() {

    const [repoId, setRepoId] = useState("");
    const [graph, setGraph] = useState(null);
    const [loading, setLoading] = useState(false);

    const loadGraph = async () => {

        if (!repoId) {
            alert("Please enter Repository ID");
            return;
        }

        try {

            setLoading(true);

            const response = await axios.post(
                `http://localhost:8000/knowledge-graph?repo_id=${repoId}`
            );

            setGraph(response.data);

        } catch (error) {

            console.log(error);

            alert("Unable to load Knowledge Graph");

        } finally {

            setLoading(false);

        }

    };

    return (

        <Layout>

            <div className="max-w-7xl">

                <h1 className="text-5xl font-bold text-amber-50 mb-3">
                    Knowledge Graph
                </h1>

                <p className="text-amber-200/70 mb-10">
                    Explore the structure of your repository including files,
                    classes, functions, methods and imports.
                </p>

                {/* Search Card */}

                <div className="bg-[#2A1E17] border border-amber-900/40 rounded-3xl p-8">

                    <div className="flex items-center gap-3 mb-6">

                        <Network size={26} />

                        <h2 className="text-2xl font-semibold">
                            Build Repository Graph
                        </h2>

                    </div>

                    <input
                        type="number"
                        placeholder="Repository ID"
                        value={repoId}
                        onChange={(e)=>setRepoId(e.target.value)}
                        className="
                            w-full
                            p-4
                            rounded-xl
                            bg-[#1A120E]
                            border
                            border-amber-900/40
                            text-white
                            outline-none
                            mb-6
                        "
                    />

                    <button
                        onClick={loadGraph}
                        disabled={loading}
                        className="
                            bg-amber-700
                            hover:bg-amber-600
                            px-6
                            py-3
                            rounded-xl
                            transition
                            disabled:opacity-50
                        "
                    >
                        {loading
                            ? "Building..."
                            : "Build Knowledge Graph"}
                    </button>

                </div>

                {graph && (

                    <>

                        {/* Summary */}

                        <div className="grid grid-cols-2 lg:grid-cols-5 gap-6 mt-10">

                            <SummaryCard
                                title="Files"
                                count={graph.files.length}
                            />

                            <SummaryCard
                                title="Classes"
                                count={graph.classes.length}
                            />

                            <SummaryCard
                                title="Functions"
                                count={graph.functions.length}
                            />

                            <SummaryCard
                                title="Methods"
                                count={graph.methods.length}
                            />

                            <SummaryCard
                                title="Imports"
                                count={graph.imports.length}
                            />

                        </div>

                        <Section
                            title="Files"
                            items={graph.files}
                        />

                        <Section
                            title="Classes"
                            items={graph.classes}
                        />

                        <Section
                            title="Functions"
                            items={graph.functions}
                        />

                        <Section
                            title="Methods"
                            items={graph.methods}
                        />

                        <Section
                            title="Imports"
                            items={graph.imports}
                        />

                    </>

                )}

            </div>

        </Layout>

    );

}

function SummaryCard({ title, count }) {

    return (

        <div
            className="
                bg-[#2A1E17]
                border
                border-amber-900/40
                rounded-3xl
                p-6
                shadow-lg
                hover:border-amber-600
                hover:scale-[1.02]
                transition-all
            "
        >

            <p className="text-amber-200/70 uppercase text-sm tracking-wide">

                {title}

            </p>

            <h1 className="text-5xl font-bold mt-4 text-white">

                {count}

            </h1>

        </div>

    );

}

function Section({ title, items }) {

    return (

        <div
            className="
                bg-[#2A1E17]
                border
                border-amber-900/40
                rounded-3xl
                p-8
                mt-10
            "
        >

            <div className="flex justify-between items-center mb-6">

                <h2 className="text-3xl font-semibold">

                    {title}

                </h2>

                <span
                    className="
                        bg-amber-700
                        px-4
                        py-2
                        rounded-full
                        text-sm
                        font-semibold
                    "
                >

                    {items.length}

                </span>

            </div>

            <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-4">

                {

                    items.slice(0,15).map((item,index)=>(

                        <div
                            key={index}
                            className="
                                bg-[#1A120E]
                                border
                                border-amber-900/40
                                rounded-2xl
                                p-4
                                break-all
                                hover:border-amber-500
                                transition-all
                            "
                        >

                            {item}

                        </div>

                    ))

                }

            </div>

            {

                items.length>15 && (

                    <div className="text-center mt-6">

                        <button
                            className="
                                bg-amber-700
                                hover:bg-amber-600
                                px-6
                                py-2
                                rounded-xl
                            "
                        >

                            + {items.length-15} More

                        </button>

                    </div>

                )

            }

        </div>

    );

}

export default KnowledgeGraph;