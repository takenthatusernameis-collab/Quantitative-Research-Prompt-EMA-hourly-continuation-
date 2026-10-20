# EMA Hourly Continuation — MEME/USDT P20_26

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1229 |
| net_profit_factor | 0.2722 |
| net_win_rate | 0.3775 |
| gross_profit_factor | 0.7678 |
| gross_win_rate | 0.4174 |
| sharpe_ratio | -13.1765 |
| sortino_ratio | -6.6379 |
| max_drawdown | 0.9998 |
| cagr | -0.9672 |
| net_avg_win | 8.0575 |
| net_avg_loss | -17.9566 |
| avg_hold_time_bars | 2.1969 |
| exposure | 0.1227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
