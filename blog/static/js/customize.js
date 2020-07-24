
//scroll down to fixed top navbar
$(document).ready(function(){
	   $(window).bind('scroll', function() {
	   	
			 if ($(window).scrollTop() > 100) {
				 $('.navbar').addClass('fixed-top');
			 }
			 else {
				 $('.navbar').removeClass('fixed-top');
			 }
		});
});

//side menu
$(document).ready(function(){
	$('.open').click(function(){
		$('.side-menu').toggleClass('dismess');
		$('.side-menu-close').toggleClass('move');
		
	});
	
});

// Search menu
$(document).ready(function(){
	$('.open-box').click(function(){
		$('.search').toggleClass('search-open');
		
	});
	
});



//your comment here.this is my main slider.
$('.owl-carousel-slider').owlCarousel({
    lazyLoad:true,
	rtl:false,
    loop:true,
	video:true,
    center:false,
	autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:false,
	autoplaySpeed:1200,
	stagePadding:0,
    responsive:{
		0:{
            items:1,
            nav:false,
			margin:0,
			dots:false,
		},
        576:{
            items:1,
            nav:false,
			margin:0,
			dots:false,
        },
        768:{
            items:1,
            nav:true,
			margin:0,
			dots:false,
        },
		992:{
            items:1,
            nav:true,
			margin:0,
			dots:false,
        },
        1200:{
            items:1,
            nav:true,
			margin:0,
			dots:false,
        }
    }
});

//your comment here. this is my testomonial slider.
$('.testimonial-slider').owlCarousel({
    lazyLoad:true,
	rtl:false,
    loop:true,
	video:true,
    center:false,
	autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true,
	autoplaySpeed:1200,
	stagePadding:0,
    responsive:{
		0:{
            items:1,
            nav:false,
			margin:0,
			dots:true,
		},
        576:{
            items:1,
            nav:false,
			margin:0,
			dots:true,
        },
        768:{
            items:1,
            nav:false,
			margin:0,
			dots:true,
        },
		992:{
            items:2,
            nav:false,
			margin:0,
			dots:true,
        },
        1200:{
            items:2,
            nav:false,
			margin:0,
			dots:true,
        }
    }
});
//your comment here.  this is my client slider.
$('.our-partners-slider').owlCarousel({
    lazyLoad:true,
	rtl:false,
    loop:true,
	video:true,
    center:false,
	autoplay:true,
    autoplayTimeout:2000,
    autoplayHoverPause:true,
	autoplaySpeed:1200,
	stagePadding: 0,
    responsive:{
		0:{
            items:2,
            nav:false,
			margin:0,
			dots:false,
		},
        576:{
            items:2,
            nav:false,
			margin:0,
			dots:false,
        },
        768:{
            items:3,
            nav:false,
			margin:0,
			dots:false,
        },
		992:{
            items:4,
            nav:false,
			margin:0,
			dots:false,
        },
        1200:{
            items:5,
            nav:false,
			margin:0,
			dots:false,
        }
    }
});