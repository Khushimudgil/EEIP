import Sidebar from "./Sidebar";

function Layout({ children }) {
  return (
    <div className="flex min-h-screen text-white bg-[#120d08] relative overflow-hidden">

      {/* Background Glow */}
      <div className="absolute top-0 left-0 w-[500px] h-[500px] bg-[#c68b59]/20 blur-[150px]" />

      <div className="absolute bottom-0 right-0 w-[500px] h-[500px] bg-[#8b5e3c]/20 blur-[150px]" />

      <Sidebar />

      <main className="flex-1 p-10 relative z-10">
        {children}
      </main>

    </div>
  );
}

export default Layout;