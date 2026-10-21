# EMA Hourly Continuation — JASMY/USDT P20_50

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.7638 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.7448 |
| sortino_ratio | -0.5346 |
| max_drawdown | 0.4918 |
| cagr | -0.2182 |
| net_avg_win | 65.3755 |
| net_avg_loss | -85.2234 |
| avg_hold_time_bars | 7.0744 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
