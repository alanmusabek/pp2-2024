!function(){function o(t){return o="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(o){return typeof o}:function(o){return o&&"function"==typeof Symbol&&o.constructor===Symbol&&o!==Symbol.prototype?"symbol":typeof o},o(t)}"object"===o(window.Pepperjam)&&null!==window.Pepperjam||(window.Pepperjam={})}();

!function(){"use strict";function t(e){if(this.constructor===t)throw new Error("Cannot instantiate abstract class");this._data=null,this.window=e}function e(e,i,a){t.call(this,e),this._cookieName=i,this._cookieMaxAge=a;var r=this;return this.getCookieName=function(){return this._cookieName},this.getCookieMaxAge=function(){return this._cookieMaxAge},this.saveData=function(t){this._data=t,this.window.document.cookie=this._cookieName+"="+t+";path=/;max-age="+this._cookieMaxAge},this.getData=function(){var t=null;return this.window.document.cookie.split(";").forEach((function(e){var i=(e=e.trim()).split("="),a=i[0],s=i[1];a===r._cookieName&&(t=s)})),t},this}function i(e,i){return t.call(this,e),this._storageKey=i,this.getStorageKey=function(){return this._storageKey},this.saveData=function(t){this._data=t,e.localStorage.setItem(this._storageKey,t)},this.getData=function(){return e.localStorage.getItem(this._storageKey)},this}function a(t,e,i){var a=t,r=e||"pjIframeParsed",s=i||[];function o(t){var e=a.document.createElement("a");return e.href=t,e}return this.getTrackingIframeUrls=function(){return function(){for(var t=[],e=a.document.querySelectorAll("iframe"),i=0;i<e.length;i++){var n=e[i],c=o(n.src),h=new RegExp(r),l=new RegExp("pjn-tracking");s.indexOf(c.hostname)>=0&&!n.className.match(h)&&!n.id.match(l)&&(t.push(c),""===n.className?n.className=r:n.className+=" "+r)}return t}()},this}function r(t){var e=t;return this.validateMessageOrigin=function(t,i){var a,r,s=(a=t.origin,(r=e.document.createElement("a")).href=a,r);return i.indexOf(s.hostname)>=0},this}t.prototype.getData=function(){return this._data},t.prototype.setData=function(t){this._data=t},e.prototype=Object.create(t.prototype),Object.defineProperty(e.prototype,"constructor",{value:e,enumerable:!1,writable:!0}),i.prototype=Object.create(t.prototype),Object.defineProperty(i.prototype,"constructor",{value:i,enumerable:!1,writable:!0}),window.PepperjamTracking=function(t){var s=this;return this.window=t,this.clickIdQueryParamIframe="CLICK_ID",this.clickIdQueryParam="clickId",this.gclidQueryParam="gclid",this.cookieName="pjn-click",this.cookieMaxAge=5184e3,this.localStorageKey="pjnClickData",this.domains=["t.pepperjamnetwork.com"],this.messageNoCookies="pjn-no-cookies",this.messageCookiesOk="pjn-cookies-ok",this.pjPrefix="p",this.gclidPrefix="g",this.iframeAdded=!1,this.maxClicks=parseInt("20"),this.lookBackPeriod=60,this.platformKey="PLATFORM",this.platform="ITC2",this.parsedIframeClass="pjIframeParsed",this.invalidClickIdRegex=/[;%&#+=?]/,this.cookieStorage=new e(this.window,this.cookieName,this.cookieMaxAge),this.localStorage=new i(this.window,this.localStorageKey),this.iframeParser=new a(this.window,this.parsedIframeClass,this.domains),this.messageValidator=new r(this.window),this.getQueryParam=function(t,e){var i=e.split("&");try{for(var a=0;a<i.length;a++){var r=i[a].split("=");if(decodeURIComponent(r[0])===t)return decodeURIComponent(r[1])}}catch(t){return!1}return!1},this.getCookieData=function(){return this.cookieStorage.getData()},this.saveCookieData=function(t){this.cookieStorage.saveData(t)},this.getLocalStorageData=function(){return this.localStorage.getData()},this.saveLocalStorageData=function(t){this.localStorage.saveData(t)},this.getClickId=function(){return this.getQueryParam(this.clickIdQueryParam,this.window.location.search.substring(1))},this.getGclid=function(){var t=this.getQueryParam(this.gclidQueryParam,this.window.location.search.substring(1));return!1!==t?t:""},this.transformClickId=function(t,e){return(e||this.pjPrefix)+t},this.getToday=function(){var t=Date.now();return Math.ceil(t/864e5)},this.getClickData=function(){var t=[],e=this.getCookieData(),i=this;if(e&&null!==e){var a=JSON.parse(e),r=this.getToday();a.forEach((function(e){i.clickWithinLookback(e,r)&&t.push(e)}))}return t},this.getPjClickData=function(){var t=this.getClickData(),e=[];return t.forEach((function(t){t.hasOwnProperty("type")&&t.type===s.pjPrefix&&e.push(t)})),e},this.clickDataToQueryParam=function(t){var e="",i=0;if("string"==typeof t&&"dynamic"===t.toLowerCase())var a=this.getClickData();else{var r=this.getClickData(),o=[];a=[],r.forEach((function(t){t.hasOwnProperty("type")&&t.type===s.gclidPrefix?a.push(t):o.push(t)})),a.push(o.pop())}return a.forEach((function(t){t&&(e+=0!==i&&t.id?","+encodeURIComponent(s.transformClickId(t.id,t.type)):encodeURIComponent(s.transformClickId(t.id,t.type)),i++)})),e||""},this.daySort=function(t,e){return(t.hasOwnProperty("days")&&t.days?t.days:0)-(e.hasOwnProperty("days")&&e.days?e.days:0)},this.mergeClickData=function(){var t=JSON.parse(this.getCookieData()),e=JSON.parse(this.getLocalStorageData()),i=this,a=[],r=[];return t&&(a=a.concat(t)),e&&(a=a.concat(e)),a.length>0&&(a=a.sort((function(t,e){return i.daySort(t,e)}))).forEach((function(t){var e=t.id,i=t.type;0===r.filter((function(t){return t.id===e&&t.type===i})).length&&r.push(t)})),this.trimCookie(r,!1)},this.handleClickId=function(t,e){var i=t;if(i&&!i.match(this.invalidClickIdRegex)){for(var a=this.getToday(),r=this.getClickData(),s=!1,o=r,n=0;n<o.length;n++)if(i===o[n].id&&e===o[n].type){s=!0;break}s||(r.push({id:i,days:a,type:e}),r.length>this.maxClicks&&(r=this.trimCookie(r,!0)),this.saveCookieData(JSON.stringify(r)))}},this.trimCookie=function(t,e){return t.length>this.maxClicks&&(t=e?(t=t.reverse().splice(0,this.maxClicks)).reverse():t.splice(0,this.maxClicks)),t},this.clickWithinLookback=function(t,e){return Math.abs(e-t.days)<=this.lookBackPeriod},this.handleConversion=function(t){if((t.data===s.messageNoCookies||t.data===s.messageCookiesOk)&&s.messageValidator.validateMessageOrigin(t,s.domains)){var e=s.iframeParser.getTrackingIframeUrls();e.length&&!s.iframeAdded&&(e.forEach((function(t,e){var i=s.window.document.createElement("iframe"),a=t.href,r=s.clickDataToQueryParam(s.getQueryParam("INT",t.search.substring(1))),o=s.getQueryParam(s.clickIdQueryParamIframe,t.search.substring(1).toUpperCase());if(o){var n=o.split(","),c=r?r.split(","):[],h=[],l=n.length,u=c.length,d=s.getPjClickData();if(s.getQueryParam("INT",t.search.substring(1))&&"dynamic"===s.getQueryParam("INT",t.search.substring(1)).toLowerCase()||0===d.length)for(e=0;e<l;e++)h.push(s.transformClickId(n[e],s.pjPrefix));for(var f=0;f<u;f++)h.indexOf(c[f])<0&&h.push(c[f]);r="";for(var g=0;g<h.length;g++)r+=h[g]+",";r=r.substr(0,r.length-1),a=a.replace(/&CLICK_ID(=[^&]*)?|^CLICK_ID(=[^&]*)?&?/i,"")}if(i.setAttribute("id","pjn-tracking-"+e),i.setAttribute("width","0"),i.setAttribute("height","0"),i.setAttribute("frameborder","0"),i.setAttribute("class",s.parsedIframeClass),t.href.match("/track/v2"))m=a;else var m=a.replace("/track","/track/v2");var p=m+"&"+s.clickIdQueryParamIframe+"="+r;p+="&"+s.platformKey+"="+s.platform,i.setAttribute("src",p),s.window.document.body.appendChild(i)})),s.iframeAdded=!0)}},this.handle=function(){this.handleClickId(this.getClickId(),this.pjPrefix),this.handleClickId(this.getGclid(),this.gclidPrefix),this.window.addEventListener("message",this.handleConversion);var t=this.mergeClickData();t&&t.length>0&&(this.saveCookieData(JSON.stringify(t)),this.saveLocalStorageData(JSON.stringify(t)))},this.setIframeParser=function(t,e,i){this.iframeParser=new a(t,e,i)},this.handle()},new window.PepperjamTracking(window)}();

usi_launch_tag="codecademy",usi_installed=0,USI_installCode=function(){if(0==usi_installed){usi_installed=1;var e=document.getElementsByTagName("head")[0],t=document.createElement("script");t.type="text/javascript",t.src="//www.upsellit.com/active/"+usi_launch_tag+".jsp",e.appendChild(t)}},void 0!==document.readyState&&"complete"===document.readyState?USI_installCode():window.addEventListener?window.addEventListener("load",USI_installCode,!0):window.attachEvent?window.attachEvent("onload",USI_installCode):USI_installCode(),setTimeout("USI_installCode()",1e4);