# EMA Hourly Continuation — TNSR/USDT P34_50

**Symbol:** TNSR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6925 |
| net_win_rate | 0.4893 |
| gross_profit_factor | 0.9673 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.2261 |
| sortino_ratio | -0.5745 |
| max_drawdown | 0.5042 |
| cagr | -0.2319 |
| net_avg_win | 68.3879 |
| net_avg_loss | -94.6180 |
| avg_hold_time_bars | 5.4190 |
| exposure | 0.0802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
