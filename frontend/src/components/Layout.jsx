import Sidebar from "./Sidebar";

function Layout({ children }) {

    return (

        <div className="min-h-screen flex bg-[#120d08] text-white">

            {/* Left Sidebar */}

            <Sidebar />

            {/* Main Content */}

            <main className="flex-1 relative overflow-auto">

                {/* Background Glow */}

                <div className="absolute inset-0 overflow-hidden pointer-events-none">

                    <div className="absolute -top-40 -left-40 w-[450px] h-[450px] rounded-full bg-[#c68b59]/10 blur-[140px]" />

                    <div className="absolute bottom-0 right-0 w-[500px] h-[500px] rounded-full bg-[#8b5e3c]/15 blur-[170px]" />

                </div>

                {/* Page Content */}

                <div className="relative z-10 max-w-7xl mx-auto px-12 py-12">

                    {children}

                </div>

            </main>

        </div>

    );

}

export default Layout;