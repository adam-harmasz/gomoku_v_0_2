$(document).ready(function () {
    var turn = 'O',
        move = 1;
        game_record_list = game_record.slice(1, -1).split(', ');
        console.log(game_record_list, swap, swap_2, color_change);
        console.log(typeof game_record_list);

    // this function will make gomoku board
    function gomoku_board_factory(data) {
        var gomoku_board = $(".gomoku-board"),
            intersection_container = $(".intersection_container"),
            coordinates_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'],
            coordinate_x,
            coordinate_y,
            rect_y = 4.5,
            rect_x,
            rect_y_intersection = 9.5,
            rect_x_intersection;

        for (i = 0; i < 15; i++) {
            coordinate_y = 15 - i;
            for (j = 0; j < 15; j++) {
                coordinate_x = coordinates_letters[j];
                rect_x = -14.5 + j * 40;
                rect_x_intersection = -0.5 + j * 40;

                // creating rect element to place possible stones, maybe to delete later
                var rect_elem_intersection = $(document.createElementNS("http://www.w3.org/2000/svg", "rect")).attr({
                    y: rect_y_intersection,
                    x: rect_x_intersection,
                    width: 40,
                    height: 40,
                    class: "board-cell-intersection-rect",
                });

                // creating circle element to place possible stones
                var circle_elem_intersection = $(document.createElementNS("http://www.w3.org/2000/svg", "circle")).attr({
                    cy: rect_y_intersection + 20,
                    cx: rect_x_intersection + 20,
                    r: 20,
                    class: "board-cell-intersection-circle",
                });

                // creating text which is hidden in default (transparent fill), fill will be change when mouse on
                var text_elem_intersection = $(document.createElementNS("http://www.w3.org/2000/svg", "text")).attr({
                    y: rect_y_intersection + 5,
                    x: rect_x_intersection,
                    class: "board-cell-intersection-coordinates",
                }).text(coordinate_x + coordinate_y);

                var g_inner_container = $(document.createElementNS("http://www.w3.org/2000/svg", "g")).attr({
                    class: "inner-intersection",
                });

                // each g inner container has unique value in combined data x and data y
                g_inner_container.attr("data-intersection-container-y", i).attr("data-intersection-container-x", j);

                // adding board cells and intersections, stones will be placed on the lines crosses
                intersection_container.append(g_inner_container);
                g_inner_container.append(rect_elem_intersection);
                g_inner_container.append(circle_elem_intersection);
                g_inner_container.append(text_elem_intersection);

                // board cells has to be limited to 14. one less than intersections due to fact that 14 cells make 15 lines
                if (i < 14 && j < 14) {
                    var rect_elem = $(document.createElementNS("http://www.w3.org/2000/svg", "rect")).attr({
                        y: rect_y,
                        x: rect_x,
                        width: 40,
                        height: 40,
                        class: "board-cell",
                    });
                    gomoku_board.append(rect_elem);
                }
            }
            rect_y = rect_y + 40;
            rect_y_intersection = rect_y_intersection + 40;
        }
    };

    // showing coordinates of mouse point when mouse over board
    function coordinates_hoover_event(data) {
        var gomoku_board_coordinates = $(".inner-intersection");
        $.each(gomoku_board_coordinates, function (i, val) {
            var text_elem = $(val).find("text"),
                g_elem_inner = $(val);
            g_elem_inner.mouseover(function () {
                text_elem.css("fill", "blue");
            });
            g_elem_inner.mouseout(function () {
                text_elem.css("fill", "transparent");
            });
            console.log($(val).find("text"));
        });
    };

    // adding stones after mouse click
    function add_next_move(data) {
        var circles = $(".next");

            circles.on('click', function (event) {
            event.preventDefault();
            turn = turn === 'O' ? 'X' : 'O';

            var _this = $(this);
            if (turn === 'O') {
                _this.css('fill', 'white');
                console.log('THIS WHITE  ', _this);
                console.log(move);
                move += 1;
            } else {
                _this.css('fill', 'black');
                console.log('THIS   ',_this);
                console.log(move);
                move += 1;
            }
        });

    }
    // Adding move on board from game record which is imported from Django back-end as context
        function add_prev_move() {
            var next_btn = $('.next');

            next_btn.on('click', function (event) {
                event.preventDefault();
                console.log(move + " który ruch");
                turn = turn === 'O' ? 'X' : 'O';
                console.log(context[move][0] + context[move][1]);
                console.log(move + 'KTÓRY RUCH');
                if (turn === 'O') {
                    $('.' + context[move][0] + '.' + context[move][1] + '').html($('<img src="' + white_src + '">'));
                    move += 1;
                    if (move === 1) {
                        prevMove();
                    } else if (move >= context.length) {
                        silenceNext();
                    }
                } else {
                    $('.' + context[move][0] + '.' + context[move][1] + '').html($('<img src="' + black_src + '">'));
                    move += 1;
                    if (move === 1) {
                        prevMove();
                    } else if (move >= context.length) {
                        silenceNext();
                    }
                }
            })
        }

    gomoku_board_factory();
    coordinates_hoover_event();
    // add_next_move();

});