# EMA Hourly Continuation — IOST/USDT P89_100

**Symbol:** IOST/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.2511 |
| net_win_rate | 0.3851 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -9.3422 |
| sortino_ratio | -3.3050 |
| max_drawdown | 0.9878 |
| cagr | -0.8268 |
| net_avg_win | 14.5224 |
| net_avg_loss | -36.2329 |
| avg_hold_time_bars | 2.4595 |
| exposure | 0.0662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
