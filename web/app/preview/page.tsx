'use client'

import { useEffect, useState } from 'react'
import ParsePreview from '../ui/parse-preview'
import axios from 'axios'
import { usePathname, useSearchParams } from 'next/navigation'

export default function Preview() {
  const searchParams = useSearchParams()
  const file_id = searchParams.get('file_id')
  const [parseResult, setParseResult] = useState('');
  

  useEffect(() => {
      const fetchOcrResults = async () => {
          if (file_id) {
              try {
                  const response = await axios.get(`http://127.0.0.1:8000/files/text_parse?file_id=${file_id}`);
                  setParseResult(response.data.parse_result);
              } catch (error) {
                  console.error('Error fetching OCR results:', error);
              }
          }
      };

      fetchOcrResults();
  }, [file_id]);
  

  return (
    <div className="note-editor">
      <div className="note-editor-form" style={{border: '1px solid #ccf'}}>
        <iframe src={`http://127.0.0.1:8000/files/static/${file_id}`} height="100%" width="100%"></iframe>
      </div>

      <div className="note-editor-preview">
        <ParsePreview>{parseResult}</ParsePreview>
      </div>
    </div>
  )
}
