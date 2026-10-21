# EMA Hourly Continuation — BAT/USDT P20_21

**Symbol:** BAT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.5048 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8495 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -3.1767 |
| sortino_ratio | -0.6834 |
| max_drawdown | 0.5506 |
| cagr | -0.2728 |
| net_avg_win | 55.0325 |
| net_avg_loss | -89.6737 |
| avg_hold_time_bars | 4.5885 |
| exposure | 0.0471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
