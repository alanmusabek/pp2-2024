(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[2479],{38846:function(t,e,r){"use strict";r.r(e),r.d(e,{__N_SSP:function(){return f}});var n=r(95235),o=r(82269),u=r(54358),c=r(4654),i=r(52322),a=["currentContentItem"];function s(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable})),r.push.apply(r,n)}return r}function l(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?s(Object(r),!0).forEach(function(e){(0,n.Z)(t,e,r[e])}):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach(function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))})}return t}var f=!0;e.default=function(t){var e=t.currentContentItem,r=(0,o.Z)(t,a);return(0,i.jsx)(c.I,l(l({},r),{},{children:(0,i.jsx)(u.L,{currentContentItem:e})}))}},54358:function(t,e,r){"use strict";r.d(e,{L:function(){return D}});var n=r(60971),o=r(95006),u=r(17722),c=r(5632),i=r(2784),a=r(56580),s=r(95235),l=r(36758),f=r(76751),p=r(20612),y=r(56795),b=r(15235),O=r(96628),g=r(71489),d=r(30911),v=r(67210),m=r(80507),j=r(52322);function h(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable})),r.push.apply(r,n)}return r}function S(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?h(Object(r),!0).forEach(function(e){(0,s.Z)(t,e,r[e])}):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):h(Object(r)).forEach(function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))})}return t}var w=function(t){var e,r=t.currentContentItem,o=t.navigateToExercise,u=(0,i.useState)(!1),s=u[0],h=u[1],w=(0,a.useDispatch)(),P=(0,a.useSelector)(O.M0),x=(0,a.useSelector)(y.hK),E=(0,m.O)(r.type),_=E.showMobileWarningWall,C=E.showMobileIntroModal,I=(0,a.useSelector)(b.ph),k=(0,c.useRouter)().query,D=k.journeySlug,N=k.pathSlug,T=D?(0,n.ay)(D):(0,n.cn)(N);return(0,i.useEffect)(function(){x&&w((0,g.K4)({type:"PaidExclusiveOverlay",returnPath:T})),_&&w((0,g.K4)({type:"MobileWarningWall",returnPath:T})),C&&w((0,g.K4)({type:"MobileIntroModal",returnPath:T}))},[w,T,x,_,C]),P.content_ids&&((e=window).dataLayer||(e.dataLayer=[]),window.dataLayer.push({event:"content_id_loaded",content_id:(0,d.I)(P.content_ids)})),(0,j.jsxs)(j.Fragment,{children:[(0,j.jsx)(l.V,{title:I}),s?(0,j.jsx)(f.e,{}):(0,j.jsx)(v.Z,{trackVisit:function(t){return(0,p.Fs)(S(S({},t),P))},exitPaths:{logo:"/",back:T},showNextContentInterstitial:function(){return h(!0)},currentContentItem:r,navigateToExercise:o})]})},P=r(40794),x=r(85819),E=r(11968),_=r(40459),C=r(10148).XA9,I=r(51244),k=function(){var t=(0,c.useRouter)().query.pathSlug,e=(0,a.useDispatch)(),r=(0,a.useSelector)(o.bB),n=(0,a.useSelector)(o.md),u=(0,a.useSelector)(o.vn),s=(0,a.useSelector)(I.Xc),l={service:x.Hj.GraphqlGateway,headers:{Authorization:"Bearer ".concat(n)}},f=(0,P.a)(C,{context:l,variables:{slug:t,userId:u,includeProgress:!!n},skip:r||s}),p=f.data,y=f.error;(0,i.useEffect)(function(){null!=p&&p.path&&e((0,_.dh)(null==p?void 0:p.path))},[null==p?void 0:p.path,e]),(0,i.useEffect)(function(){y&&(0,E.H)(y)},[y])},D=function(t){var e=t.currentContentItem,r=(0,c.useRouter)(),s=r.push,l=r.query,f=l.pathSlug,p=l.trackSlug,y=l.moduleSlug,b=l.contentItemSlug,O=(0,a.useSelector)(o.bB);k();var g=(0,i.useCallback)(function(t){s((0,n.Ne)({pathSlug:f,trackSlug:p,moduleSlug:y,contentItemSlug:b,exerciseSlug:t}),void 0,{shallow:!0})},[f,p,y,b,s]);return!e||O?(0,j.jsx)(u.o,{}):(0,j.jsx)(w,{navigateToExercise:g,currentContentItem:e})}},9635:function(t,e,r){"use strict";r.d(e,{s:function(){return v}});var n=r(92952),o=r(22900),u=r(94368),c=r(2784),i=r(52322);function a(t){return(a="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(t)}function s(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter(function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable})),r.push.apply(r,n)}return r}function l(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?s(Object(r),!0).forEach(function(e){var n,o;n=e,o=r[e],(n=function(t){var e=function(t,e){if("object"!==a(t)||null===t)return t;var r=t[Symbol.toPrimitive];if(void 0!==r){var n=r.call(t,e||"default");if("object"!==a(n))return n;throw TypeError("@@toPrimitive must return a primitive value.")}return("string"===e?String:Number)(t)}(t,"string");return"symbol"===a(e)?e:String(e)}(n))in t?Object.defineProperty(t,n,{value:o,enumerable:!0,configurable:!0,writable:!0}):t[n]=o}):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):s(Object(r)).forEach(function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))})}return t}function f(){return(f=Object.assign?Object.assign.bind():function(t){for(var e=1;e<arguments.length;e++){var r=arguments[e];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(t[n]=r[n])}return t}).apply(this,arguments)}var p={1:1,2:2,3:3,4:4,5:5,6:6},y={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11},b=u.CA.create({rowOffset:{property:"gridRowStart",scale:p,transform:function(t){return 0===t?"auto":t}},rowspan:{property:"gridRowEnd",scale:p,transform:function(t){return"span ".concat(t)}},size:{property:"gridColumnEnd",scale:l(l({},y),{},{12:12}),transform:function(t){return"span ".concat(t)}},offset:{property:"gridColumnStart",scale:l({0:0},y),transform:function(t){return 0===t?"auto":"".concat(t+1)}}}),O=(0,o.bU)({variants:{fitContent:{display:"grid",gridTemplateColumns:"minmax(0, 1fr)"}}}),g=u.CA.compose(o.By.layout,o.By.space,o.By.grid,o.By.list,b),d=(0,n.Z)("div",f({},{target:"e1y0e4q30",label:"StyledColumn"},(0,o.Nb)(g.propNames)))(g({size:12}),O,g,""),v=(0,c.forwardRef)(function(t,e){var r=t.variant,n=function(t,e){if(null==t)return{};var r,n,o=function(t,e){if(null==t)return{};var r,n,o={},u=Object.keys(t);for(n=0;n<u.length;n++)r=u[n],e.indexOf(r)>=0||(o[r]=t[r]);return o}(t,e);if(Object.getOwnPropertySymbols){var u=Object.getOwnPropertySymbols(t);for(n=0;n<u.length;n++)r=u[n],!(e.indexOf(r)>=0)&&Object.prototype.propertyIsEnumerable.call(t,r)&&(o[r]=t[r])}return o}(t,["variant"]);return(0,i.jsx)(d,l({variant:void 0===r?"fitContent":r,ref:e},n))})},21314:function(t,e,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/paths/[pathSlug]/tracks/[trackSlug]/modules/[moduleSlug]/[contentItemType]/[contentItemSlug]/exercises/[exerciseSlug]",function(){return r(38846)}])}},function(t){t.O(0,[2928,831,9498,9894,740,2981,7336,9097,8059,7935,7144,8895,8819,8294,8890,6256,3675,632,7426,472,6310,9774,2888,179],function(){return t(t.s=21314)}),_N_E=t.O()}]);
//# sourceMappingURL=[exerciseSlug]-e8cb916a8c601c19.js.map