$(document).ready(function () {
    var turn = 'O',
        move = 0;
        game_record_list = game_record.slice(1, -1).split(', ');
        console.log(color_change);
        console.log(typeof game_record_list);

    // this function will make gomoku board
    function gomoku_board_factory(data) {
        var gomoku_board = $(".gomoku-board"),
            intersection_container = $(".intersection_container"),
            coordinates_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
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
                    id: "" + coordinate_x + coordinate_y + "",

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

    // adding next move from the game record after mouse click
    function add_next_move(data) {
        var next_btn = $("#next");
            console.log(move);
            next_btn.on('click', function (event) {
                event.preventDefault();
                turn = turn === 'O' ? 'X' : 'O';
                if (move <= game_record_list.length) {
                    if (turn === 'O') {
                        $('#'.concat(game_record_list[move].slice(1, -1))).css('fill', 'white');
                        console.log("asdasd", move);
                        move += 1;
                        if (move === 1) {
                            undo_move();
                        } else if (move >= game_record_list.length) {
                            silenceNext();
                        }
                    } else {
                        $('#'.concat(game_record_list[move].slice(1, -1))).css('fill', 'black');
                        console.log(move);
                        move += 1;
                        if (move === 1) {
                            undo_move();
                        } else if (move >= game_record_list.length) {
                            silenceNext();
                        }
                    }

                }

            })
    }
    // undo move on board according to game record
    function undo_move() {
        var undo_btn = $('#undo');
            console.log(move);
            undo_btn.on('click', function (event) {
                event.preventDefault();
                turn = turn === 'O' ? 'X' : 'O';

                if (move === game_record_list.length) {
                    silenceNext();
                    add_next_move();
                }
                move -= 1;
                $('#'.concat(game_record_list[move].slice(1, -1))).css('fill', 'transparent');
                    console.log("asdasd", move);
                if (move === 0) {
                    silenceUndo();
                }
            })
    }

    // show all moves at once
        function lastMove() {
            var last_button = $('#end');

            last_button.on('click', function (event) {
                event.preventDefault();
                turn = 'O';
                move = 0;
                for (var i = 0; i < game_record_list.length; i++){
                    turn = turn === 'O' ? 'X' : 'O';
                    if (turn === 'O') {
                        $('#'.concat(game_record_list[move].slice(1, -1))).css('fill', 'white');
                        move += 1;
                    } else {
                        $('#'.concat(game_record_list[move].slice(1, -1))).css('fill', 'black');
                        move += 1;
                    }
                }
                console.log(move + "  który mamy ruch");
                silenceUndo();
                undo_move();
                silenceNext();
                silenceLast();
            });
        }

    // function enabling events
    function initGame() {
        var start = $('#start');
        move = 0;
        start.one('click', function (event) {
            event.preventDefault();
            add_next_move();
            coordinates_hoover_event();
            console.log('start!');
        })
    }

    // function removing click event from next button
    function silenceNext() {
        $('#next').off('click');
    }

        // function removing click event from next button
    function silenceUndo() {
        $('#undo').off('click');
    }

    function silenceLast() {
        $('#end').off('click');
    }

    initGame();
    gomoku_board_factory();
});