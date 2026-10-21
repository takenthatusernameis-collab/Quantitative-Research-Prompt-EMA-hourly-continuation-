# EMA Hourly Continuation — ZRX/USDT P8_100

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7546 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9529 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.0245 |
| sortino_ratio | -0.6508 |
| max_drawdown | 0.5516 |
| cagr | -0.2599 |
| net_avg_win | 65.4826 |
| net_avg_loss | -83.4302 |
| avg_hold_time_bars | 29.1575 |
| exposure | 0.6733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
