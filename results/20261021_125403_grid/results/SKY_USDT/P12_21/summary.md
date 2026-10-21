# EMA Hourly Continuation — SKY/USDT P12_21

**Symbol:** SKY/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.5327 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8370 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -4.2960 |
| sortino_ratio | -1.3019 |
| max_drawdown | 0.7113 |
| cagr | -0.4502 |
| net_avg_win | 49.3831 |
| net_avg_loss | -75.1776 |
| avg_hold_time_bars | 4.4533 |
| exposure | 0.0904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
