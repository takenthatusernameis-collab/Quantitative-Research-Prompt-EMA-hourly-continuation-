# EMA Hourly Continuation — CATI/USDT P21_26

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.2822 |
| net_win_rate | 0.3268 |
| gross_profit_factor | 0.6408 |
| gross_win_rate | 0.3800 |
| sharpe_ratio | -16.5234 |
| sortino_ratio | -8.8889 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 10.6537 |
| net_avg_loss | -18.3300 |
| avg_hold_time_bars | 1.9832 |
| exposure | 0.1227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
