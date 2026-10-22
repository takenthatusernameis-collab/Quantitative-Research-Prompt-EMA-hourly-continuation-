# EMA Hourly Continuation — PENDLE/USDT P34_100

**Symbol:** PENDLE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.6048 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -4.1352 |
| sortino_ratio | -1.5248 |
| max_drawdown | 0.8444 |
| cagr | -0.5161 |
| net_avg_win | 39.8547 |
| net_avg_loss | -58.6119 |
| avg_hold_time_bars | 8.9620 |
| exposure | 0.2786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
