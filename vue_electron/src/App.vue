<template>
  <div>
    <input ref="fileInput" type="file" multiple />
    <button @click="uploadFiles">Upload</button>
    <div v-if="uploadProgress !== null">
      {{ uploadProgress }}%
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios, { AxiosResponse } from 'axios';

export default defineComponent({
  data() {
    return {
      uploadProgress: null as null | number,
    };
  },
  methods: {
    async uploadFiles() {
      const files = (this.$refs.fileInput as HTMLInputElement).files;
      if (!files || files.length === 0) {
        return;
      }

      // Iterate through each file
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const chunkSize = 100000000; // 100MB
        const numChunks = Math.ceil(file.size / chunkSize);
        let chunkIndex = 0;
        let offset = 0;

        // Iterate through each chunk
        while (chunkIndex < numChunks) {
          const chunk = file.slice(offset, offset + chunkSize);
          const formData = new FormData();
          formData.append('file', chunk);
          formData.append('file_name', file.name);
          formData.append('chunk_index', chunkIndex.toString());
          formData.append('num_chunks', numChunks.toString());

          try {
            const res: AxiosResponse = await axios.post('http://localhost:8000/upload', formData, {
              onUploadProgress: (progressEvent) => {
                // const percentCompleted = Math.round(
                //   (progressEvent.loaded * 100) / progressEvent.total
                // );
                console.log(i + ' / ' + files.length);
                this.uploadProgress = Math.round((progressEvent.progress as number)*100);
              },
            });
            console.log(res.data);
          } catch (error) {
            console.error(error);
          }

          chunkIndex++;
          offset += chunkSize;
        }
      }

      this.uploadProgress = null;
    },
  },
});
</script>
