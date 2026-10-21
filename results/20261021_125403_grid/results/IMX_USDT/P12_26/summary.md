# EMA Hourly Continuation — IMX/USDT P12_26

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7653 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -1.9643 |
| sortino_ratio | -0.6181 |
| max_drawdown | 0.5729 |
| cagr | -0.2467 |
| net_avg_win | 68.5324 |
| net_avg_loss | -91.0473 |
| avg_hold_time_bars | 5.7531 |
| exposure | 0.1255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
