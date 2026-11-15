# EMA Hourly Continuation — CERE/USDT P26_89

**Symbol:** CERE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 796 |
| net_profit_factor | 0.4592 |
| net_win_rate | 0.3618 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.3920 |
| sharpe_ratio | -9.7279 |
| sortino_ratio | -3.8857 |
| max_drawdown | 0.9938 |
| cagr | -0.8663 |
| net_avg_win | 29.3003 |
| net_avg_loss | -36.1705 |
| avg_hold_time_bars | 9.3405 |
| exposure | 0.3380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
