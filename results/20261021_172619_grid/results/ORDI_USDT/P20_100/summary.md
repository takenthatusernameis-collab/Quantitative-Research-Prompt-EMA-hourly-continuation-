# EMA Hourly Continuation — ORDI/USDT P20_100

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7204 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -2.3033 |
| sortino_ratio | -0.7091 |
| max_drawdown | 0.5726 |
| cagr | -0.2782 |
| net_avg_win | 66.0505 |
| net_avg_loss | -79.6358 |
| avg_hold_time_bars | 18.1535 |
| exposure | 0.3870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
