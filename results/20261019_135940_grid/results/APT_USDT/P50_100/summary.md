# EMA Hourly Continuation — APT/USDT P50_100

**Symbol:** APT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.5878 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -4.4884 |
| sortino_ratio | -1.6269 |
| max_drawdown | 0.8620 |
| cagr | -0.5406 |
| net_avg_win | 38.9661 |
| net_avg_loss | -61.0471 |
| avg_hold_time_bars | 5.3405 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
