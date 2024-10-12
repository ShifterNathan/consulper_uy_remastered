import { useState, useEffect } from "react";

export default function useFetchServices(url: string) {
  const [data, setData] = useState<any>(null);
  const [error, setError] = useState<Error | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const response = await fetch(url);
        const data = await response.json();
        setData(data);
        setError(null);
      } catch (error) {
        console.error("Fetch error:", error);
        setData(null);
        setError(error as Error);
      }
      setIsLoading(false);
    };
    fetchData();
  }, [url]);

  return { isLoading, error, data };
}