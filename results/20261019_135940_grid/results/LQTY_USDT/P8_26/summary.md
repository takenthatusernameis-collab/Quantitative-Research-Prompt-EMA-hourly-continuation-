# EMA Hourly Continuation — LQTY/USDT P8_26

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1510 |
| net_profit_factor | 0.4458 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8257 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -9.5363 |
| sortino_ratio | -5.1893 |
| max_drawdown | 0.9985 |
| cagr | -0.9237 |
| net_avg_win | 11.9333 |
| net_avg_loss | -21.5244 |
| avg_hold_time_bars | 4.4119 |
| exposure | 0.3015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
