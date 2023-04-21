$(document).ready(function() {
    // Check if dark mode is enabled in local storage and set it
    if (localStorage.getItem('darkMode') == 'on') {
        $('body,.slider_section,.header_section,.footer_section').addClass('dark');
        $('.change').text('ON');
    } else {
        $('body,.slider_section,.header_section,.footer_section').removeClass('dark');
        $('.change').text('OFF');
    }
    
    // Handle dark mode toggle
    $('.change').on('click', function() {
        if ($('body,.slider_section,.header_section,.footer_section').hasClass('dark')) {
            $('body,.slider_section,.header_section,.footer_section').removeClass('dark');
            $('.change').text('OFF');
            localStorage.setItem('darkMode', 'off');
        } else {
            $('body,.slider_section,.header_section,footer_section').addClass('dark');
            $('.change').text('ON');
            localStorage.setItem('darkMode', 'on');
        }
    });
});
