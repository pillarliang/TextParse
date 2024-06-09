'use client'

import React, { useState } from 'react';
import { UploadOutlined } from '@ant-design/icons';
import { message, Upload, Button } from 'antd';
import axios from 'axios';
import { useRouter } from 'next/navigation';


export default function UploadFile() {
  const [fileList, setFileList] = useState<any[]>([]);
  const router = useRouter(); // 使用新的 useRouter 钩子

  const customRequest = async (options:any) => {
    const { onSuccess, onError, file, onProgress } = options;
    const formData = new FormData();
    formData.append('file', file);
  
    try {
      const response = await axios.post('http://127.0.0.1:8000/files/upload', formData, {
        onUploadProgress: ({ total, loaded }) => {
          onProgress({ percent: Math.round((loaded / total!) * 100).toFixed(2) }, file);
        },
      });
  
      onSuccess(response, file);
      message.success('Upload successfully');
      router.push(`/preview?file_id=${response.data.uuid_filename}`);
    } catch (error) {
      onError({ error });
      message.error('Upload failed');
    }
  };
  
  
  const handleChange = (info:any) => {
    let fileList = [...info.fileList];
    fileList = fileList.slice(-1);
    fileList = fileList.map(file => {
      if (file.response?.data) {
        file.url = file.response.data.url;
        file.name = file.response.data.filename;
      }
      return file;
    });
    setFileList(fileList);
  };

  return (
    <Upload
      className='ant-upload'
      accept='.pdf,image/*'
      listType='picture'
      customRequest={customRequest}
      onChange={handleChange}
      fileList={fileList}
    >
      <Button icon={<UploadOutlined />} className='ant-upload-btn'>Click to upload File</Button>
    </Upload>
  )
}
