# EMA Hourly Continuation — ADA/USDT P89_100

**Symbol:** ADA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.1794 |
| net_win_rate | 0.3625 |
| gross_profit_factor | 0.5708 |
| gross_win_rate | 0.4072 |
| sharpe_ratio | -10.0289 |
| sortino_ratio | -3.5498 |
| max_drawdown | 0.9916 |
| cagr | -0.8505 |
| net_avg_win | 10.2731 |
| net_avg_loss | -32.5690 |
| avg_hold_time_bars | 1.9656 |
| exposure | 0.0520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
