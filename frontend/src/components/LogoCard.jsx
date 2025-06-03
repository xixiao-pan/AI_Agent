export default function LogoCard({ data }) {
    return (
      <div style={{ margin: "10px 0" }}>
        <p>{data.prompt}</p>
        <img src={"http://localhost:8000" + data.image_path} width="150" />
      </div>
    );
  }