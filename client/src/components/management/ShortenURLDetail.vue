<template>
    <div class="modal left fade" id="modalDetail" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 id="myModalLabel">Detail</h1>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                        aria-hidden="true"><i class="bi bi-x-lg"></i></span></button>
                </div>
                <div class="text-center pt-4 pb-4">
                    <a href="#">
                        short.url
                        <span>/1sdas8df1</span>
                    </a>
                    <div class="pt-2">
                        <button id="copyBtn" type="button" class="btn btn-primary btn-sm"><i
                            class="bi bi-clipboard"></i> Copy
                        </button>
                        <button id="redirectBtn" type="button" class="btn btn-danger btn-sm"><i
                            class="bi bi-box-arrow-in-right"></i> Go to
                        </button>
                    </div>
                </div>
                <div class="modal-body">
                    <div>
                        <h4>Total click: 456</h4>
                        <chartjs-bar :labels="dataTotalClick.labels" :datasets="dataTotalClick.datasets"></chartjs-bar>
                    </div>
                    <br>
                    <div>
                        <h4>Location: </h4>
                        <chartjs-pie :labels="dataLocation.labels" :datasets="dataLocation.datasets"
                                     :option="dataLocation.options"></chartjs-pie>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="submit" class="btn btn-success" id="edit">Save</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Utils from "moment";

const labels = Utils.weekdays();

export default {
    name: "ShortenURLDetail",
    data() {
        return {
            isCustomizeBackHalf: false,
            dataTotalClick     : {
                labels  : labels,
                datasets: [{
                    label          : 'Date Created',
                    data           : [65, 59, 80, 81, 56, 55, 40, 0, 0, 16],
                    backgroundColor: [
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(153, 102, 255, 1)',
                    ],
                }],
            },
            dataLocation       : {
                options : {
                    responsive: true,
                    plugins   : {
                        legend: {
                            position: 'top',
                        },
                        title : {
                            display: true,
                            text   : 'Chart.js Pie Chart'
                        }
                    }
                },
                labels  : ['Viet Nam', 'Japan', 'USA', 'China', 'Singapore'],
                datasets: [
                    {
                        label          : 'Dataset 1',
                        data           : [20, 30, 40, 50, 70],
                        backgroundColor: ['Red', 'Orange', 'Yellow', 'Green', 'Blue'],
                    }
                ]
            },
        }
    }
}
</script>

<style scoped>
#edit {
    width: 100% !important;
    height: 3rem !important;
}

#copyBtn, #redirectBtn {
    width: 30% !important;
}

.text-center {
    border-bottom: 1px solid lightgray;
}
</style>
