import { Textarea } from "@material-tailwind/react";
import { useState } from "react";
import FileUpload from "react-material-file-upload";

export default function FileUploads() {
  const [files, setFiles] = useState<File[]>([]);
  return (
    <div className="FileUploads">
      <h1 className="pt-10 pb-5"> File Upload</h1>
      <div className="pt-5 pb-5">

        <FileUpload value={files} onChange={setFiles} />
      </div>
      <div className="pb-5">
        <div className="pb-10">

        Tranlation
        </div>
      <Textarea  aria-label="empty textarea" placeholder="Translated text" className="pt-5" sty/>
      </div>
    </div>
  );
}