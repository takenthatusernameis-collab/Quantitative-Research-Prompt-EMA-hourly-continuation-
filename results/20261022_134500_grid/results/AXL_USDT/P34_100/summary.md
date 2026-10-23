# EMA Hourly Continuation — AXL/USDT P34_100

**Symbol:** AXL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.5878 |
| net_win_rate | 0.4405 |
| gross_profit_factor | 0.8838 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -5.4319 |
| sortino_ratio | -2.0520 |
| max_drawdown | 0.9197 |
| cagr | -0.6289 |
| net_avg_win | 40.6443 |
| net_avg_loss | -54.4425 |
| avg_hold_time_bars | 8.4200 |
| exposure | 0.2785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
