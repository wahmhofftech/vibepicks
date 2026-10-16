// "What are we building today?" recommender. 100% client-side keyword matching: no AI, no API calls, nothing tracked.
(function(root){
const KW={
'app-builders':{3:['website','web site','site','webpage','web page','landing page','homepage','store','shop online','online store','ecommerce','e-commerce','app','application','portfolio','blog','booking','bakery','restaurant','business','small business','tracker','track','dashboard','crm','inventory','form','directory','marketplace','prototype','mvp','idea','no code','nocode','beginner','simple','phone','mobile','iphone','android','tool','game'],1:['menu','calendar','schedule','quote','invoice','customers','jobs']},
'coding-agents':{3:['code','coding','program','programming','script','refactor','fix my','bug','debug','repo','github','developer','python','javascript','typescript','react','existing','extension','plugin','automate','automation','automatic','workflow','workflows','zapier','excel','macro','scrape','scraper','bot','cli','game','api'],1:['app','tool','learn']},
'hosting':{3:['host','hosting','deploy','publish','launch','go live','online','domain','put it online','server','live','website','web site'],1:['site','landing page','blog','portfolio']},
'auth':{3:['login','log in','log-in','sign in','signin','sign up','signup','account','accounts','users','user','password','members','membership','member','customer portal','portal'],1:['private','secure']},
'databases':{3:['database','data','save','store data','records','backend','back end','inventory','spreadsheet','track','tracker','crm','orders','customers','jobs','list','storage','upload'],1:['dashboard','booking','app']},
'design-to-code':{3:['design','figma','mockup','mock up','look','pretty','beautiful','ui','ux','layout','brand','branding','style','screen','sketch','wireframe','colors'],1:['landing page','website','portfolio']},
'testing':{3:['test','testing','tests','bug','bugs','broken','crash','crashes','error','errors','qa','quality','check','review','monitor'],1:[]},
'ai-images':{5:['emote','emotes','twitch emote','sticker','stickers','logo','thumbnail','thumbnails','avatar','avatars','profile picture','pfp','illustration','illustrations','game art','game assets','sprite','sprites','fan art','ai art'],3:['twitch','stream','streamer','streaming','youtube','art','artwork','drawing','draw','image','images','picture','pictures','photo','photos','icon','icons','banner','poster','cartoon','character','characters','meme','memes','graphic','graphics','video','videos','tiktok','reels','badge','badges','overlay','merch','t-shirt','tattoo'],1:['brand','branding','design','channel']},
'ai-audio':{5:['jingle','jingles','voiceover','voiceovers','voice over','narration','narrate','podcast','podcasts','song','songs','music','beat','beats','text to speech','tts','transcribe','transcript','transcription','sound effect','sound effects'],3:['voice','voices','audio','sound','sounds','intro','outro','lyrics','speech','singing','rap','soundtrack','background music','audiobook','dub','dubbing'],1:['youtube','video','stream']},
'ai-hardware':{5:['arduino','esp32','esp8266','raspberry pi','raspberry','stm32','nucleo','blue pill','cubeide','embedded','plc','plcs','ladder logic','allen bradley','allen-bradley','siemens','codesys','openplc','hmi','conveyor','rpi','pi zero','pi 4','pi 5','raspi','linux board','single board computer','pico','microcontroller','sensor','sensors','circuit','circuits','pcb','circuit board','wiring','breadboard','robot','robots','robotics','iot','3d print','3d printing','3d printer','cnc','electronics','hardware','firmware','soldering','led','leds','servo','motor','smart home','home automation'],3:['wireless','bluetooth','wifi','wi-fi','lora','gadget','device','drone','lathe','machine','mill','plc','relay','battery','solder'],1:['physical','build']},
'llm-apis':{5:['chatbot','chat bot','support bot','customer service'],3:['email','emails','essay','copy','copywriting','caption','captions','story','stories','newsletter','content','chat','ai','gpt','assistant','answer questions','customer service','support bot','summarize','summary','write','writing','generate','translate','llm','model','api','agent','agents','smart','recommend','pdf','documents'],1:['bot','automate','automation']},
};
const norm=s=>' '+String(s||'').toLowerCase().replace(/[^a-z0-9+#.\- ]+/g,' ').replace(/\s+/g,' ')+' ';
function score(text){const t=norm(text),out={};
 for(const id in KW)for(const w in KW[id])for(const k of KW[id][w]){
  const re=new RegExp('(^|[^a-z])'+k.replace(/[.*+?^${}()|[\]\\-]/g,'\\$&')+'(s|es|ing|ed)?(?=[^a-z]|$)');
  if(re.test(t))out[id]=(out[id]||0)+(+w)}
 return out}
const BOARDS=[
['pi',/(raspberry|\brpi\b|\braspi\b|\bpi (zero|[2345])\b|linux board|single board computer|python on (a |my )?pi)/,/\bpico\b/,[['ChatGPT',"Tell it your Pi model and parts and it walks you through the wiring to the GPIO pins and writes the Python for you. Send a photo of your setup if something isn't working."],
['Cursor',"An AI code editor for your Pi's Python. Connect to the Pi over SSH from your main computer and the AI edits and fixes code right on the board."],
['Claude Code',"An AI helper that works in the terminal and can set up, write and debug Python projects on your Pi. Best once you're comfortable with the command line."]]],
['plc',/(\bplcs?\b|ladder logic|allen.bradley|siemens|codesys|openplc|\bhmi\b|structured text)/,null,[['OpenPLC',"A free, open-source PLC you can program with ladder logic or structured text, so you can build and test your logic on a PC or Raspberry Pi before touching real equipment."],
['ChatGPT',"Describe your machine, inputs and outputs and it lays out the ladder logic or structured text step by step and explains each rung. Always test before running real equipment."]]],
['stm32',/(stm32|nucleo|blue pill|cubeide|\bhal\b)/,null,[['ChatGPT',"Name your STM32 chip and parts and it explains the wiring and writes the C code (HAL) for timers, PWM and sensors, and helps when it won't compile."],
['Wokwi',"Simulates some STM32 chips in your browser, including the Blue Pill (STM32F103C8), so you can test code before flashing a real board."],
['Claude Code',"An AI helper that can read your whole STM32 project folder and write or fix the C code across files. Best once you're comfortable with the command line."]]],
['mcu',/(arduino|esp32|esp8266|\bpico\b|\buno\b|\bnano\b|microcontroller)/,null,null],
['generic',/./,null,[['ChatGPT',"Describe your parts and what you want them to do and it explains the wiring and writes the code, whatever board you use. Send a photo if something isn't working."],
['Tinkercad',"A free, beginner-friendly way to design parts to 3D print and practice simple circuits on screen."],
['Wokwi',"If your project uses a common board like Arduino, ESP32, Pi Pico or STM32, you can test it in your browser before buying parts."]]]];
function boardTools(text,D){const t=norm(text);const b=BOARDS.find(([,re,not])=>re.test(t)&&!(not&&not.test(t)));if(!b[3])return null;const all=D.categories.flatMap(c=>c.tools);return b[3].map(([n,why])=>{const x=all.find(x=>x.name===n);return x&&Object.assign({},x,{why})}).filter(Boolean)}
function recommend(text,D){const bt=boardTools(text,D);const s=score(text),cats=D.categories.filter(c=>s[c.id]>=3).sort((a,b)=>s[b.id]-s[a.id]||D.categories.indexOf(a)-D.categories.indexOf(b));
 if(!cats.length){const g=D.categories;return{matched:false,picks:[{c:g.find(c=>c.id==='app-builders'),tools:[0,1]},{c:g.find(c=>c.id==='coding-agents'),tools:[0,1]}].map(p=>({cat:p.c,tools:p.tools.map(i=>p.c.tools[i])}))}}
 return{matched:true,picks:cats.slice(0,3).map((c,i)=>({cat:c,score:s[c.id],tools:(bt&&c.id==='ai-hardware')?bt.slice(0,i===0?3:2):c.tools.slice(0,i===0?3:2)}))}}
root.VPReco={score,recommend,KW};
if(typeof module!=='undefined')module.exports=root.VPReco;
})(typeof window!=='undefined'?window:globalThis);
