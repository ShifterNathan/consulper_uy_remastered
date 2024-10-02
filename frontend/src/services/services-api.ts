import { ref } from "vue";

export default function useFetchServices(url: string) {
  const data = ref();
  const error = ref();
  const isLoading = ref(false);

  async function fetchData() {
    isLoading.value = true;
    try {
      const response = await fetch(url);
      const services = await response.json();
      data.value = services;
      error.value = undefined;
    } catch (err) {
      console.error("Fetch error:", err);
      data.value = undefined;
      error.value = err;
    }
    isLoading.value = false;
  }
  fetchData();

  return { isLoading, error, data };
}