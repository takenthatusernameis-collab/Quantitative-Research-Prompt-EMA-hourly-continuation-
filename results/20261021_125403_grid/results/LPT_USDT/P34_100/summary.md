# EMA Hourly Continuation — LPT/USDT P34_100

**Symbol:** LPT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6868 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -2.6681 |
| sortino_ratio | -0.8216 |
| max_drawdown | 0.6210 |
| cagr | -0.3152 |
| net_avg_win | 61.7164 |
| net_avg_loss | -78.3602 |
| avg_hold_time_bars | 11.9893 |
| exposure | 0.2550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
