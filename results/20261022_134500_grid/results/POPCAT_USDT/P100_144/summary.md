# EMA Hourly Continuation — POPCAT/USDT P100_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5900 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8716 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -4.0261 |
| sortino_ratio | -1.3052 |
| max_drawdown | 0.7439 |
| cagr | -0.4657 |
| net_avg_win | 51.0698 |
| net_avg_loss | -72.9525 |
| avg_hold_time_bars | 3.9431 |
| exposure | 0.0952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
