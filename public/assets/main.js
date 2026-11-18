// Reha for Dogs – Menü, Einblendungen, Telefonzeiten
function menue(){
  const m=document.getElementById("mobil"),b=document.querySelector(".burger");
  const auf=m.classList.toggle("offen");
  b.setAttribute("aria-expanded",auf);
  b.setAttribute("aria-label",auf?"Menü schließen":"Menü öffnen");
  b.innerHTML=auf
    ?'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>'
    :'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  document.body.style.overflow=auf?"hidden":"";
}
document.querySelectorAll("#mobil a").forEach(a=>a.addEventListener("click",()=>{if(document.getElementById("mobil").classList.contains("offen"))menue()}));

// Leistungen-Menü per Tastatur/Touch
document.querySelectorAll(".dd>button").forEach(b=>b.addEventListener("click",e=>{
  const d=b.parentElement,auf=d.classList.toggle("offen");b.setAttribute("aria-expanded",auf);e.stopPropagation();
}));
document.addEventListener("click",()=>document.querySelectorAll(".dd.offen").forEach(d=>{d.classList.remove("offen");d.querySelector("button").setAttribute("aria-expanded","false")}));

// sanftes Einblenden
const io="IntersectionObserver" in window?new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("on");io.unobserve(e.target)}}),{rootMargin:"0px 0px -8% 0px"}):null;
document.querySelectorAll(".rv").forEach(el=>io?io.observe(el):el.classList.add("on"));

// Telefonzeiten Mo–Fr 9–18 Uhr (Zeitzone Berlin)
(function(){
  const s=document.getElementById("status");if(!s)return;
  try{
    const t=new Intl.DateTimeFormat("de-DE",{timeZone:"Europe/Berlin",weekday:"short",hour:"2-digit",minute:"2-digit",hour12:false}).formatToParts(new Date());
    const w=t.find(p=>p.type==="weekday").value,h=+t.find(p=>p.type==="hour").value,m=+t.find(p=>p.type==="minute").value;
    const werktag=["Mo","Di","Mi","Do","Fr"].some(x=>w.startsWith(x)),min=h*60+m;
    if(werktag&&min>=540&&min<1080){s.classList.add("an");s.lastElementChild.textContent="Jetzt telefonisch erreichbar"}
    else s.lastElementChild.textContent="Telefonisch wieder ab "+(werktag&&min<540?"heute":"dem nächsten Werktag")+" 9:00 Uhr";
  }catch(e){}
})();
const j=document.getElementById("jahr");if(j)j.textContent=new Date().getFullYear();
