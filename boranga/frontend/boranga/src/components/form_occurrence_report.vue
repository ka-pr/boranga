<template lang="html">
    <div>
        <div class="" :id="occurrenceReportBody">
            <OCRProfile ref="ocr_profile" id="ocrProfile" :is_external="is_external" :referral="referral"
                :show_observer_contact_information="show_observer_contact_information"
                :occurrence_report_obj="occurrence_report_obj" @refreshOccurrenceReport="refreshOccurrenceReport()">
            </OCRProfile>
            <SubmitterInformation v-if="occurrence_report_obj.submitter_information" :key="reloadcount"
                ref="submitter_information" id="submitter_information"
                :show_submitter_contact_details="show_submitter_contact_details"
                :submitter_information="occurrence_report_obj.submitter_information"
                :disabled="!occurrence_report_obj.can_user_edit" />
        </div>
        <div class="col-md-12">
            <ul id="pills-tab" class="nav nav-pills" role="tablist">
                <li class="nav-item">
                    <a id="pills-location-tab" class="nav-link active" data-bs-toggle="pill" :href="'#' + locationBody"
                        role="tab" :aria-controls="locationBody" aria-selected="true" @click="tabClicked()">
                        Location
                    </a>
                </li>
                <li class="nav-item">
                    <a id="pills-habitat-tab" class="nav-link" data-bs-toggle="pill" :href="'#' + habitatBody"
                        role="tab" aria-selected="false" @click="tabClicked()">
                        Habitat
                    </a>
                </li>
                <li class="nav-item">
                    <a id="pills-observation-tab" class="nav-link" data-bs-toggle="pill" :href="'#' + observationBody"
                        role="tab" aria-selected="false" @click="tabClicked()">
                        Observation
                    </a>
                </li>
                <li class="nav-item">
                    <a id="pills-documents-tab" class="nav-link" data-bs-toggle="pill" :href="'#' + documentBody"
                        role="tab" aria-selected="false" @click="tabClicked()">
                        Documents
                    </a>
                </li>
                <li class="nav-item">
                    <a id="pills-threats-tab" class="nav-link" data-bs-toggle="pill" :href="'#' + threatBody" role="tab"
                        aria-selected="false" @click="tabClicked()">
                        Threats
                    </a>
                </li>
            </ul>
            <div id="pills-tabContent" class="tab-content">
                <div :id="locationBody" class="tab-pane fade show active" role="tabpanel"
                    aria-labelledby="pills-location-tab">
                    <OCRLocation id="ocrLocation" :key="reloadcount" ref="ocr_location" :is_external="is_external"
                        :is_internal="is_internal" :can-edit-status="canEditStatus"
                        :occurrence_report_obj="occurrence_report_obj" :referral="referral"
                        @refreshFromResponse="refreshFromResponse">
                    </OCRLocation>
                </div>
                <div :id="habitatBody" class="tab-pane fade" role="tabpanel" aria-labelledby="pills-habitat-tab">
                    <OCRHabitat id="ocrhabitat" :key="reloadcount" ref="ocr_habitat" :is_internal="is_internal"
                        :is_external="is_external" :occurrence_report_obj="occurrence_report_obj">
                    </OCRHabitat>
                </div>
                <div :id="observationBody" class="tab-pane fade" role="tabpanel"
                    aria-labelledby="pills-observation-tab">
                    <OCRObservation id="ocrObservation" :key="reloadcount" ref="ocr_observation"
                        :is_internal="is_internal" :is_external="is_external"
                        :occurrence_report_obj="occurrence_report_obj">
                    </OCRObservation>
                </div>
                <div :id="documentBody" class="tab-pane fade" role="tabpanel" aria-labelledby="pills-documents-tab">
                    <OCRDocuments id="ocrDocuments" :key="reloadcount" ref="ocr_documents" :is_internal="is_internal"
                        :is_external="is_external" :occurrence_report_obj="occurrence_report_obj">
                    </OCRDocuments>
                </div>
                <div :id="threatBody" class="tab-pane fade" role="tabpanel" aria-labelledby="pills-threats-tab">
                    <OCRThreats id="ocrThreats" :key="reloadcount" ref="ocr_threats" :is_internal="is_internal"
                        :is_external="is_external" :occurrence_report_obj="occurrence_report_obj">
                    </OCRThreats>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import OCRLocation from '@/components/common/occurrence/ocr_location.vue';
import OCRHabitat from '@/components/common/occurrence/ocr_habitat.vue';
import OCRObservation from '@/components/common/occurrence/ocr_observation.vue';
import SubmitterInformation from '@/components/common/submitter_information.vue'
import OCRDocuments from '@/components/common/occurrence/ocr_documents.vue';
import OCRThreats from '@/components/common/occurrence/ocr_threats.vue';
import OCRProfile from '@/components/common/occurrence/occurrence_report_profile.vue';

export default {
    components: {
        OCRLocation,
        OCRHabitat,
        OCRObservation,
        OCRDocuments,
        OCRThreats,
        OCRProfile,
        SubmitterInformation,
    },
    props: {
        occurrence_report_obj: {
            type: Object,
            required: true,
        },
        referral: {
            type: Object,
            required: false,
        },
        is_external: {
            type: Boolean,
            default: false,
        },
        is_internal: {
            type: Boolean,
            default: false,
        },
        canEditStatus: {
            type: Boolean,
            default: true,
        },
        show_observer_contact_information: {
            type: Boolean,
            default: true,
        },
    },
    emits: ['refreshFromResponse', 'refreshOccurrenceReport'],
    data: function () {
        let vm = this;
        return {
            values: null,
            reloadcount: 0,
            occurrenceReportBody: 'occurrenceReportBody' + vm._uid,
            locationBody: 'locationBody' + vm._uid,
            habitatBody: 'habitatBody' + vm._uid,
            observationBody: 'observationBody' + vm._uid,
            threatBody: 'threatBody' + vm._uid,
            documentBody: 'documentBody' + vm._uid,
            relatedItemBody: 'relatedItemBody' + vm._uid,
        };
    },
    computed: {
        show_submitter_contact_details: function () {
            return 'OccurrenceReportReferral' != this.$parent.$options.name
        },
        related_items_ajax_url: function () {
            return (
                '/api/occurrence_report/' +
                this.occurrence_report_obj.id +
                '/get_related_items/'
            );
        },
        related_items_filter_list_url: function () {
            return '/api/occurrence_report/filter_list.json';
        },
    },
    mounted: function () {
        let vm = this;
        vm.form = document.forms.new_occurrence_report;
        vm.eventListener();
    },
    methods: {
        //----function to resolve datatable exceeding beyond the div
        // eslint-disable-next-line no-unused-vars
        tabClicked: function (param) {
            this.reloadcount = this.reloadcount + 1;
        },
        eventListener: function () {
            // eslint-disable-next-line no-unused-vars
            let vm = this;
        },
        // eslint-disable-next-line no-unused-vars
        refreshFromResponse: function (data) {
            //this.$emit('refreshFromResponse', data);
        },
        refreshOccurrenceReport: function () {
            this.$emit('refreshOccurrenceReport');
        },
    },
};
</script>

<style lang="css" scoped>
.section {
    text-transform: capitalize;
}

.list-group {
    margin-bottom: 0;
}

.fixed-top {
    position: fixed;
    top: 56px;
}

.nav-item {
    margin-bottom: 2px;
}

.nav-item>li>a {
    background-color: yellow !important;
    color: #fff;
}

.nav-item>li.active>a,
.nav-item>li.active>a:hover,
.nav-item>li.active>a:focus {
    color: white;
    background-color: blue;
    border: 1px solid #888888;
}

.admin>div {
    display: inline-block;
    vertical-align: top;
    margin-right: 1em;
}

.nav-pills .nav-link {
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    border-top-left-radius: 0.5em;
    border-top-right-radius: 0.5em;
    margin-right: 0.25em;
}

.nav-pills .nav-link {
    background: lightgray;
}

.nav-pills .nav-link.active {
    background: gray;
}
</style>
