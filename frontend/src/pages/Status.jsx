import { useState } from "react";
import { Activity, CheckCircle, Loader2 } from "lucide-react";
import Layout from "../components/Layout";
import api from "../services/api";

function Status() {

    const [repoId, setRepoId] = useState("");
    const [status, setStatus] = useState(null);
    const [loading, setLoading] = useState(false);

    const checkStatus = async () => {

        if (!repoId) {
            alert("Please enter Repository ID");
            return;
        }

        try {

            setLoading(true);

            const response = await api.get(
                `/repository/${repoId}/status`
            );

            setStatus(response.data);

        } catch (error) {

            console.error(error);

            alert("Unable to fetch repository status.");

        } finally {

            setLoading(false);

        }

    };

    return (

        <Layout>

            <div className="max-w-5xl">

                <h1 className="text-5xl font-bold text-amber-50 mb-3">

                    Repository Status

                </h1>

                <p className="text-amber-200/70 mb-10">

                    Monitor indexing progress of your repository.

                </p>

                <div className="bg-[#2A1E17] border border-amber-900/40 rounded-3xl p-8">

                    <div className="flex items-center gap-3 mb-6">

                        <Activity size={24} />

                        <h2 className="text-2xl font-semibold">

                            Check Repository Status

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
                        onClick={checkStatus}
                        disabled={loading}
                        className="
                            flex
                            items-center
                            gap-2
                            bg-amber-700
                            hover:bg-amber-600
                            px-6
                            py-3
                            rounded-xl
                            transition
                            disabled:opacity-50
                        "
                    >

                        {

                            loading

                            ?

                            <Loader2 className="animate-spin" size={18}/>

                            :

                            <Activity size={18}/>

                        }

                        {

                            loading

                            ?

                            "Checking..."

                            :

                            "Check Status"

                        }

                    </button>

                </div>

                {

                    status &&

                    <div className="mt-10 bg-[#2A1E17] border border-amber-900/40 rounded-3xl p-8">

                        <div className="flex items-center gap-3 mb-8">

                            <CheckCircle
                                className="text-green-400"
                                size={28}
                            />

                            <h2 className="text-3xl font-semibold">

                                Repository Details

                            </h2>

                        </div>

                        <div className="grid md:grid-cols-2 gap-6">

                            <InfoCard
                                title="Repository ID"
                                value={status.id}
                            />

                            <InfoCard
                                title="Status"
                                value={status.status}
                            />

                            <InfoCard
                                title="Repository URL"
                                value={status.repo_url}
                            />

                            <InfoCard
                                title="Progress"
                                value={
                                    status.status==="READY"
                                    ? "100%"
                                    : "Processing..."
                                }
                            />

                        </div>

                        {

                            status.status==="READY"

                            &&

                            <div className="mt-8">

                                <div className="w-full h-4 rounded-full bg-[#1A120E] overflow-hidden">

                                    <div className="h-full w-full bg-green-500 rounded-full"></div>

                                </div>

                                <p className="text-green-400 mt-3">

                                    Repository indexing completed successfully.

                                </p>

                            </div>

                        }

                    </div>

                }

            </div>

        </Layout>

    );

}

function InfoCard({title,value}){

    return(

        <div className="bg-[#1A120E] rounded-2xl p-5 border border-amber-900/40">

            <p className="text-amber-200/70 mb-2">

                {title}

            </p>

            <h3 className="text-lg font-semibold break-all">

                {value}

            </h3>

        </div>

    );

}

export default Status;