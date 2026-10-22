# EMA Hourly Continuation — RIO/USDT P20_100

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.8096 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -1.6444 |
| sortino_ratio | -0.5256 |
| max_drawdown | 0.5271 |
| cagr | -0.2170 |
| net_avg_win | 81.7463 |
| net_avg_loss | -90.6474 |
| avg_hold_time_bars | 15.7904 |
| exposure | 0.3632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
