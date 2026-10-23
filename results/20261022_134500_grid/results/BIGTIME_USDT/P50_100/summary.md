# EMA Hourly Continuation — BIGTIME/USDT P50_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.9816 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -3.9308 |
| sortino_ratio | -1.3570 |
| max_drawdown | 0.8181 |
| cagr | -0.4740 |
| net_avg_win | 51.4484 |
| net_avg_loss | -71.1354 |
| avg_hold_time_bars | 7.1960 |
| exposure | 0.1944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
