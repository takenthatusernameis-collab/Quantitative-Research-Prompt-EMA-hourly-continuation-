# EMA Hourly Continuation — ERG/USDT P12_89

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6952 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.8660 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -2.3382 |
| sortino_ratio | -0.7498 |
| max_drawdown | 0.5877 |
| cagr | -0.2923 |
| net_avg_win | 55.1379 |
| net_avg_loss | -71.2948 |
| avg_hold_time_bars | 19.4773 |
| exposure | 0.4489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
