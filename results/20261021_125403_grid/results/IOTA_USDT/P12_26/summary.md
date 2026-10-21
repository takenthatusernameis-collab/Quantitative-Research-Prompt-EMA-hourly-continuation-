# EMA Hourly Continuation — IOTA/USDT P12_26

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7608 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0747 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -2.2521 |
| sortino_ratio | -0.7599 |
| max_drawdown | 0.6151 |
| cagr | -0.2930 |
| net_avg_win | 65.8094 |
| net_avg_loss | -90.6945 |
| avg_hold_time_bars | 5.2896 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
