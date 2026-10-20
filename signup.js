/* VibePicks signup: generic .nlf forms + phone sticky bar */
(function(){
var K='vp_nl_done',C='vp_bar_closed';
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){}}
function form(id){return '<form class="nlf" novalidate><input type="email" name="email" placeholder="you@example.com" required aria-label="Email address"><input type="text" name="company" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0"><button class="btn">Send it to me</button></form><p class="note nlmsg" role="status">No spam. Unsubscribe anytime.</p>'}
window.vpForm=form;
document.addEventListener('submit',async function(e){var f=e.target;if(!f.classList||!f.classList.contains('nlf'))return;e.preventDefault();
var m=f.parentNode.querySelector('.nlmsg'),b=f.querySelector('button'),t=b.textContent,em=f.email.value.trim();
if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em)){m.textContent='Please enter a valid email address.';m.style.color='#f87171';return}
b.disabled=true;b.textContent='Sending…';
try{var r=await fetch('/api/subscribe',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:em,company:f.company.value})}),j=await r.json();
if(j.ok){window.va&&window.va('event',{name:'signup',data:{where:f.dataset.where||'card'}});m.textContent="You're in! Watch for the next VibePicks.";m.style.color='#4ade80';f.reset();ls(K,'1');hide()}
else{m.textContent=j.error||'Something went wrong.';m.style.color='#f87171'}}catch(x){m.textContent='Network error, please try again.';m.style.color='#f87171'}
b.disabled=false;b.textContent=t},true);
var bar;
function hide(){if(bar)bar.classList.remove('show')}
function mk(){if(bar||ls(K)||ls(C))return;bar=document.createElement('div');bar.className='nlbar';bar.setAttribute('role','region');bar.setAttribute('aria-label','Newsletter signup');
bar.innerHTML='<div class="nlbar-row"><span>Free weekly email: AI tools worth trying</span><button type="button" class="btn nlbar-go">Sign up</button><button type="button" class="nlbar-x" aria-label="Close">×</button></div><div class="nlbar-form" hidden>'+form()+'</div>';
document.body.appendChild(bar);
bar.querySelector('.nlbar-x').onclick=function(){ls(C,'1');hide()};
bar.querySelector('.nlbar-go').onclick=function(){var s=document.getElementById('subscribe');
if(s&&s.offsetParent){hide();s.scrollIntoView({behavior:'smooth',block:'center'});var i=s.querySelector('input[type=email]');i&&setTimeout(function(){i.focus()},400)}
else{var fd=bar.querySelector('.nlbar-form');fd.hidden=false;bar.querySelector('.nlbar-go').style.display='none';fd.querySelector('input').focus()}};
}
function chk(){if(!window.matchMedia('(max-width:640px)').matches||ls(K)||ls(C))return hide();
var h=document.documentElement,p=(h.scrollTop||document.body.scrollTop)/Math.max(1,h.scrollHeight-h.clientHeight);
if(p>=0.3){mk();if(bar){var fe=bar.querySelector('form');if(fe)fe.dataset.where='bar';bar.classList.add('show')}}}
addEventListener('scroll',chk,{passive:true});addEventListener('resize',chk);
})();
