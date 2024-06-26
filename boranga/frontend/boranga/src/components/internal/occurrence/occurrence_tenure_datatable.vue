<template>
    <div id="occurrence_tenure_datatable_template">
        <CollapsibleFilters
            ref="collapsible_filters"
            component_title="Filters"
            :collapsed="!filterApplied"
            @created="collapsible_component_mounted"
        >
            <div class="row">
                <div class="col-md-3">
                    <div class="form-group">
                        <label for="occurrence_tenure_feature_id_lookup"
                            >Feature ID:</label
                        >
                        <select
                            id="occurrence_tenure_feature_id_lookup"
                            ref="occurrence_tenure_feature_id_lookup"
                            name="occurrence_tenure_feature_id_lookup"
                            class="form-control"
                        />
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="form-group">
                        <label
                            for="occurrence_tenure_status_lookup"
                            class="text-nowrap"
                            >Status:</label
                        >
                        <select
                            ref="occurrence_tenure_status_lookup"
                            v-model="filterStatus"
                            class="form-select"
                        >
                            <option value="all">All</option>
                            <option
                                v-for="status in tenure_statuses"
                                :key="status.value"
                                :value="status.value"
                            >
                                {{ status.name }}
                            </option>
                        </select>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="form-group">
                        <label for="occurrence_tenure_vesting_lookup"
                            >Vesting:</label
                        >
                        <select
                            id="occurrence_tenure_vesting_lookup"
                            ref="occurrence_tenure_vesting_lookup"
                            name="occurrence_tenure_vesting_lookup"
                            class="form-control"
                        />
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="form-group">
                        <label for="occurrence_tenure_purpose_lookup"
                            >Purpose:</label
                        >
                        <select
                            id="occurrence_tenure_purpose_lookup"
                            ref="occurrence_tenure_purpose_lookup"
                            name="occurrence_tenure_purpose_lookup"
                            class="form-control"
                        />
                    </div>
                </div>
            </div>
        </CollapsibleFilters>
        <datatable
            :id="datatable_id"
            ref="occurrence_tenure_datatable"
            :dt-options="options"
            :dt-headers="headers"
        />
    </div>
</template>

<script>
import { api_endpoints, constants, helpers } from '@/utils/hooks';
import datatable from '@/utils/vue/datatable.vue';
import { v4 as uuid } from 'uuid';
import CollapsibleFilters from '@/components/forms/collapsible_component.vue';

export default {
    name: 'OccurrenceTenureDatatable',
    components: {
        datatable,
        CollapsibleFilters,
    },
    emit: ['highlight-on-map', 'edit-tenure-details'],
    props: {
        occurrenceId: {
            type: Number,
            required: false,
            default: null,
        },
        hrefContainerId: {
            type: String,
            required: false,
            default: '',
        },
        filterStatusCache: {
            type: String,
            required: false,
            default: 'occurrence_tenure_status_filter_cache',
        },
        filterFeatureIdCache: {
            type: String,
            required: false,
            default: 'occurrence_tenure_feature_id_filter_cache',
        },
        filterVestingCache: {
            type: String,
            required: false,
            default: 'occurrence_tenure_vesting_filter_cache',
        },
        filterPurposeCache: {
            type: String,
            required: false,
            default: 'occurrence_tenure_purpose_filter_cache',
        },
    },
    data: function () {
        return {
            uuid: uuid(),
            datatable_id: 'occurrence-tenure-datatable-' + uuid(),
            url: api_endpoints.occurrence_tenure_paginated_internal,
            headers: [
                'Feature ID',
                // 'Tenure Area ID',
                'Status',
                'Vesting',
                'Purpose',
                'Signif. to OCC',
                'Comments',
                "Owner's Name",
                // 'Owner Count',
                'Updated',
                'Action',
            ],
            tenure_statuses: [
                { value: 'current', name: 'Current' },
                { value: 'historical', name: 'Historical' },
            ],
            filterStatus: sessionStorage.getItem(this.filterStatusCache)
                ? sessionStorage.getItem(this.filterStatusCache)
                : 'all',
            filterFeatureId: sessionStorage.getItem(this.filterFeatureIdCache)
                ? sessionStorage.getItem(this.filterFeatureIdCache)
                : 'all',
            filterVesting: sessionStorage.getItem(this.filterVestingCache)
                ? sessionStorage.getItem(this.filterVestingCache)
                : 'all',
            filterPurpose: sessionStorage.getItem(this.filterPurposeCache)
                ? sessionStorage.getItem(this.filterPurposeCache)
                : 'all',
        };
    },
    computed: {
        filterApplied: function () {
            let allFiltersAreAll = [
                this.filterFeatureId,
                this.filterStatus,
                this.filterVesting,
                this.filterPurpose,
            ].every((filter) => ['all'].includes(filter));

            return !allFiltersAreAll;
        },
        column_featureid: function () {
            return {
                data: 'featureid',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_tenure_area_id: function () {
            return {
                data: 'tenure_area_id',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_owner_name: function () {
            return {
                data: 'owner_name',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_vesting: function () {
            return {
                data: 'vesting',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_purpose: function () {
            return {
                data: 'purpose',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_comments: function () {
            return {
                data: 'comments',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_significant_to_occurrence: function () {
            return {
                data: 'significant_to_occurrence',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_status: function () {
            return {
                data: 'status_display',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_datetime_updated: function () {
            return {
                data: 'datetime_updated',
                orderable: true,
                searchable: true,
                visible: true,
            };
        },
        column_action: function () {
            const vm = this;
            return {
                data: 'id',
                orderable: false,
                searchable: false,
                visible: true,
                // eslint-disable-next-line no-unused-vars
                render: function (data, type, row) {
                    const coordinates = row.tenure_area_centroid
                        ? JSON.stringify(row.tenure_area_centroid.coordinates)
                        : '';
                    let html = `<a href="#${vm.hrefContainerId}" class="btn btn-primary btn-sm mb-1" data-highlight-on-map-coordinates="${coordinates}">Highlight on Map</a>`;
                    html += `<br><a href="#" class="btn btn-primary btn-sm" data-edit-tenure-details="${data}">Edit Tenure Details</a>`;
                    return html;
                },
            };
        },
        options: function () {
            let columns = [
                this.column_featureid,
                // this.column_tenure_area_id,
                this.column_status,
                this.column_vesting,
                this.column_purpose,
                this.column_significant_to_occurrence,
                this.column_comments,
                this.column_owner_name,
                // this.column_owner_count,
                this.column_datetime_updated,
                this.column_action,
            ];
            let url = this.url;
            if (this.occurrenceId) {
                url = `${this.url}&occurrence_id=${this.occurrenceId}`;
            }
            return {
                autoWidth: false,
                language: {
                    processing: constants.DATATABLE_PROCESSING_HTML,
                },
                responsive: true,
                searching: true,
                ordering: true,
                order: [
                    [1, 'asc'],
                    [7, 'desc'],
                    [0, 'desc'],
                ],
                fixedColumns: {
                    start: 1,
                    end: 1,
                },
                paging: true,
                ajax: {
                    url: url,
                    dataSrc: 'data',
                    data: (d) => {
                        d.filter_status = this.filterStatus;
                        d.tenure_area_id = this.filterFeatureId;
                        d.vesting = this.filterVesting;
                        d.purpose = this.filterPurpose;
                    },
                },
                dom:
                    "<'d-flex align-items-center'<'me-auto'l>fB>" +
                    "<'row'<'col-sm-12'tr>>" +
                    "<'d-flex align-items-center'<'me-auto'i>p>",
                buttons: [
                    {
                        extend: 'excel',
                        text: '<i class="fa-solid fa-download"></i> Excel',
                        className: 'btn btn-primary me-2 rounded',
                        exportOptions: {
                            orthogonal: 'export',
                        },
                    },
                    {
                        extend: 'csv',
                        text: '<i class="fa-solid fa-download"></i> CSV',
                        className: 'btn btn-primary rounded',
                        exportOptions: {
                            orthogonal: 'export',
                        },
                    },
                ],
                columns: columns,
                processing: true,
                // eslint-disable-next-line no-unused-vars
                initComplete: function (settings, json) {
                    //
                },
            };
        },
    },
    watch: {
        filterStatus: function () {
            this.$refs.occurrence_tenure_datatable.vmDataTable.ajax.reload(
                helpers.enablePopovers,
                false
            );
            sessionStorage.setItem(this.filterStatusCache, this.filterStatus);
        },
        filterFeatureId: function () {
            this.$refs.occurrence_tenure_datatable.vmDataTable.ajax.reload(
                helpers.enablePopovers,
                false
            );
            sessionStorage.setItem(
                this.filterFeatureIdCache,
                this.filterFeatureId
            );
        },
        filterVesting: function () {
            this.$refs.occurrence_tenure_datatable.vmDataTable.ajax.reload(
                helpers.enablePopovers,
                false
            );
            sessionStorage.setItem(this.filterVestingCache, this.filterVesting);
        },
        filterPurpose: function () {
            this.$refs.occurrence_tenure_datatable.vmDataTable.ajax.reload(
                helpers.enablePopovers,
                false
            );
            sessionStorage.setItem(this.filterPurposeCache, this.filterPurpose);
        },
        filterApplied: function () {
            if (this.$refs.collapsible_filters) {
                this.$refs.collapsible_filters.show_warning_icon(
                    this.filterApplied
                );
            }
        },
    },
    mounted: function () {
        this.$nextTick(() => {
            // Make this a loop
            const filterLookupParameters = [
                {
                    ref: 'occurrence_tenure_feature_id_lookup',
                    vModelDataProperty: 'filterFeatureId',
                    placeholder: 'Select a feature ID',
                },
                {
                    ref: 'occurrence_tenure_vesting_lookup',
                    vModelDataProperty: 'filterVesting',
                    placeholder: 'Select a vesting',
                },
                {
                    ref: 'occurrence_tenure_purpose_lookup',
                    vModelDataProperty: 'filterPurpose',
                    placeholder: 'Select a purpose',
                },
            ];
            filterLookupParameters.forEach((parameters) => {
                this.initialiseFilterLookup(...Object.values(parameters));
            });

            this.addEventListeners();
        });
    },
    methods: {
        addEventListeners: function () {
            const vm = this;
            this.$refs.occurrence_tenure_datatable.vmDataTable.on(
                'click',
                'a[data-highlight-on-map-coordinates]',
                function (e) {
                    let coordinates = $(this).attr(
                        'data-highlight-on-map-coordinates'
                    );
                    coordinates = coordinates || null;
                    if (!coordinates) {
                        e.preventDefault();
                    }
                    vm.highlightOnMap(coordinates);
                }
            );
            this.$refs.occurrence_tenure_datatable.vmDataTable.on(
                'click',
                'a[data-edit-tenure-details]',
                function (e) {
                    e.preventDefault();
                    const id = $(this).attr('data-edit-tenure-details');
                    vm.editTenureDetails(id);
                    console.log(id);
                }
            );
        },
        highlightOnMap: function (coordinates = null) {
            this.$emit('highlight-on-map', JSON.parse(coordinates));
        },
        editTenureDetails: function (id) {
            this.$emit('edit-tenure-details', id);
        },
        collapsible_component_mounted: function () {
            this.$refs.collapsible_filters.show_warning_icon(
                this.filterApplied
            );
        },
        /**
         * Initialises the select2 dropdown for this filter lookup
         * @param {String} ref The ref of the select html element
         * @param {String} vModelDataProperty The selected value will be stored in this property or v-model
         * @param {String=} placeholder A placeholder text for the select2 dropdown
         * @param {String=} apiEndpoint The api endpoint to fetch the data from, defaults to `ref`
         */
        initialiseFilterLookup: function (
            ref,
            vModelDataProperty,
            placeholder = 'Select a value',
            apiEndpoint = null
        ) {
            const vm = this;
            if (!this.$refs[ref]) {
                console.error(
                    `The ref ${ref} does not exist in the component.`
                );
                return;
            }
            if (vm[vModelDataProperty] === undefined) {
                console.error(
                    `The property ${vModelDataProperty} does not exist in the component.`
                );
                return;
            }
            if (!apiEndpoint) {
                apiEndpoint = ref;
            }

            const sessionStorageText =
                this.sessionStorageText(vModelDataProperty);

            $(this.$refs[ref])
                .select2({
                    minimumInputLength: 2,
                    theme: 'bootstrap-5',
                    allowClear: true,
                    placeholder: placeholder,
                    ajax: {
                        url: api_endpoints[apiEndpoint],
                        dataType: 'json',
                        data: function (params) {
                            var query = {
                                term: params.term,
                                type: 'public',
                                occurrence_id: vm.occurrenceId,
                            };
                            return query;
                        },
                    },
                })
                .on('select2:select', function (e) {
                    let data = e.params.data.id;
                    vm[vModelDataProperty] = data;
                    sessionStorage.setItem(
                        sessionStorageText,
                        e.params.data.text
                    );
                })
                .on('select2:unselect', function () {
                    vm[vModelDataProperty] = 'all';
                    sessionStorage.setItem(sessionStorageText, '');
                })
                .on('select2:open', function () {
                    const searchField = $(
                        `[aria-controls="select2-${ref}-results"]`
                    );
                    searchField[0].focus();
                });

            // Add the stored selected value to the select2 dropdown if it exists
            const sessionStorageItem = sessionStorage.getItem(
                this.sessionStorageText(vModelDataProperty)
            );
            if (!['all', null].includes(sessionStorageItem)) {
                const newOption = new Option(
                    sessionStorageItem,
                    this[vModelDataProperty],
                    false,
                    true
                );
                this.$refs[ref].append(newOption);
            }
        },
        sessionStorageText: function (key) {
            return `${key}Text`;
        },
    },
};
</script>
