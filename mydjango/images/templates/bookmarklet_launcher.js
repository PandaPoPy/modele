/**
 * Created by popy on 28/09/16.
 */
(function(){

    if (window.myBookmarklet !== undefined){

        myBookmarklet();

    }
    else {

        document.body.appendChild(document.createElement('script')).

            src='http://mysite.com:8000/images/static/js/bookmarklet.js?r='+Math.

            floor(Math.random()*99999999999999999999);

    }

})();