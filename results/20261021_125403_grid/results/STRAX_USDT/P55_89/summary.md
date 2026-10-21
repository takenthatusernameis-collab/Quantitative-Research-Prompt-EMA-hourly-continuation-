# EMA Hourly Continuation — STRAX/USDT P55_89

**Symbol:** STRAX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.5594 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8441 |
| gross_win_rate | 0.4408 |
| sharpe_ratio | -3.9404 |
| sortino_ratio | -1.0727 |
| max_drawdown | 0.7130 |
| cagr | -0.3926 |
| net_avg_win | 56.8443 |
| net_avg_loss | -79.2049 |
| avg_hold_time_bars | 7.6364 |
| exposure | 0.1267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
