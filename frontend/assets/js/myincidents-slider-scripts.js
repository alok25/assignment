    $(document).on("click", ".myIncidentSlide", function() {
        if ($(".myIncidentPan").hasClass('moveRight')) {
            $(".myIncidentPan").removeClass("moveRight");
            $(".myIncidentPan").animate({
                left: "-85%"
            });
            $(".blkBg").hide();
        } else {
            $(".myIncidentPan").addClass("moveRight");
            $(".myIncidentPan").animate({
                left: "0"
            });
            $(".blkBg").show();
        }
    });

    $(document).on("click", ".notifiSlide", function() {
        if ($(".notificationPan").hasClass('moveLeft')) {
            $(".notificationPan").removeClass("moveLeft");
            $(".notificationPan").animate({
                right: "-85%"
            });
            $(".blkBg").hide();
        } else {
            $(".notificationPan").addClass("moveLeft");
            $(".notificationPan").animate({
                right: "0"
            });
            $(".blkBg").show();
        }
    });

    $(document).on("click", ".blkBg", function() {
        $(".notificationPan").removeClass("moveLeft");
        $(".notificationPan").animate({
            right: "-2000"
        });
        $(".myIncidentPan").removeClass("moveRight");
        $(".myIncidentPan").animate({
            left: "-2000"
        });
        $(this).hide();

    });

    $(document).on("click", ".closeNotification", function() {
        $(".notificationPan").removeClass("moveLeft");
        $(".notificationPan").animate({
            right: "-2000"
        });
        $(".blkBg").hide();
    });

    $(document).on("click", ".closeMyIncident", function() {
        $(".myIncidentPan").removeClass("moveRight");
        $(".myIncidentPan").animate({
            left: "-2000"
        });
        $(".blkBg").hide();
    });

    $(document).on("click", ".help", function() {
        $(this).next(".tooltipWindow").toggle();
    });

    $(document).on("click", ".closePan", function() {
        $(this).parent(".tooltipWindow").hide();
    });

    $(document).on("click", ".responseLink", function() {
        if ($(this).hasClass('collapsed')) {
            $(".responseList").hide();
        } else {
            $(".responseList").show();
        }
    });

    $(document).on("click", ".noteLink,.linkedAnswer", function() {
        $(".responseList").hide();
    });

    $(document).on("click", ".responseList .panel-title a", function() {
        if ($(".responseList .panel-collapse").hasClass('in')) {
        } else {
            $(".responseHead").show();
        }
        if($('.responseList .panel-title a[aria-expanded*="true"]').length == 0){
            $(".responseList .panel-collapse").removeClass('in');
            $('.responseList h4 a span').hide();
        }

    });
    $(document).on("click", "#close-right-slider", function() {
        $(".responseList .panel-collapse").removeClass('in');
        $(".responseHead").hide();
    });

    $('html').click(function(e) {
        if ($(".myIncidentPan").hasClass('moveRight')) {
            $(".myIncidentPan").removeClass("moveRight");
            $(".myIncidentPan").animate({
                left: "-85%"
            });
            $(".blkBg").hide();
            e.stopPropagation();
        }

    });
