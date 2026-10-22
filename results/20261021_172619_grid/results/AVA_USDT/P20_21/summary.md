# EMA Hourly Continuation — AVA/USDT P20_21

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 150 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8197 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -2.3175 |
| sortino_ratio | -0.4074 |
| max_drawdown | 0.3887 |
| cagr | -0.1705 |
| net_avg_win | 63.8633 |
| net_avg_loss | -98.6497 |
| avg_hold_time_bars | 4.0733 |
| exposure | 0.0278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
