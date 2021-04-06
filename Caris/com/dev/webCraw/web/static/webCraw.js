"use strict";
/**
 * @Web-Crawling-Service-Loginc
 */

/**
 * @초기화
 */
$(document).ready(function () {
    $('#_searchBtn').attr("disabled",true);
});

/**
 * @키적용
 */
$(document).on('keypress' ,function (e) {
    if (e.which === 13) {
        fn.searchWord();
    }
});

/**
 * @desc 조회할 사이트명을 입력 받아 크롤링 요청  Func.
 * @type {*|jQuery|HTMLElement}
 */
const fn = {
    searchWord : function () {
        let _search = $('#_searchText').val();
        let _chk = valCheck.fc_validation_check(_search);

        if (_chk) {
            let _url = "/craw"
            let dataSet = {};
            dataSet.word = _search;

            let getJson = JSON.stringify(dataSet);
            console.debug("getJson : ", getJson);

            $.ajax({
                type: "POST",
                url: _url,
                data: getJson,
                async : false,
                contentType: "application/json"
                })
                 .done(function (data, status) {
                     fn.searchCallback(data, status);
                    });
            } else {
                $('#_searchText').val('');
            }
        },

    /**
     * @desc 크롤링이 완료되면 활성홫 된 후 크롤링된 데이터를 조회하는 Func.
     * @type {*|jQuery|HTMLElement}
     */
    searchData : function () {
        alert("서비스 준비중..")
    },

    searchCallback : function (data, status) {
        if (status === 'success') {
            console.debug("data : ", data);
            if (data.statusCode === '200') {
                alert("크롤링이 정상적으로 완료되었습니다!");
            } else {
                alert("크롤링 서비스가 처리되지 않았습니다. 관리자에게 문의해주세요.");
            }
            let dataList = data.dataList;
            console.debug(dataList);
            alert(dataList);
            $('#_searchText').attr("disabled",false);
            $('#_searchPage').attr("disabled",false);
            $('#_searchBtn').attr("disabled",false);
            $('#_searchText').val('');
        } else {
            alert("검색어 조회에 실패하였습니다..");
        }
    }
}

/**
 * @desc 검색어 입력 text validation 체크 Func.
 * @type {{fc_validation_check: (function(*=): boolean)}}
 */
const valCheck = {
    fc_validation_check : function(param) {
        console.debug(param);
        let check = false;
        if (param === '' || param === undefined || param === "") {
            alert("검색어를 입력해주세요..");
        } else {
            check = true;
        }
        return check;
    }
}




