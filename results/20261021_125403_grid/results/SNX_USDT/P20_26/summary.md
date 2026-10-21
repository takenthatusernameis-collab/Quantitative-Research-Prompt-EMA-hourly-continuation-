# EMA Hourly Continuation — SNX/USDT P20_26

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.8213 |
| net_win_rate | 0.5433 |
| gross_profit_factor | 1.1816 |
| gross_win_rate | 0.5433 |
| sharpe_ratio | -0.8528 |
| sortino_ratio | -0.1780 |
| max_drawdown | 0.2764 |
| cagr | -0.0782 |
| net_avg_win | 75.5398 |
| net_avg_loss | -109.3989 |
| avg_hold_time_bars | 4.4087 |
| exposure | 0.0415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
