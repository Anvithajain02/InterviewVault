const BASE=import.meta.env.VITE_API_BASE_URL||"http://127.0.0.1:8000/api";
export async function apiRequest(path,options={}) {
 const headers={...(options.headers||{})};
 if(options.body && !(options.body instanceof FormData)) headers["Content-Type"]="application/json";
 if(options.token) headers.Authorization=`Bearer ${options.token}`;
 const body=options.body && typeof options.body!=="string" && !(options.body instanceof FormData)?JSON.stringify(options.body):options.body;
 const response=await fetch(`${BASE}${path}`,{...options,headers,body});
 const ct=response.headers.get("content-type")||"";
 const payload=ct.includes("application/json")?await response.json():await response.text();
 if(!response.ok) { const message=typeof payload==="object"?(payload.detail||Object.entries(payload).map(([k,v])=>`${k}: ${Array.isArray(v)?v.join(", "):v}`).join(" | ")):payload; throw new Error(message||`Request failed (${response.status})`); }
 return payload;
}
