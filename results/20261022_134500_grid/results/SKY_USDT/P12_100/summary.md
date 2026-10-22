# EMA Hourly Continuation — SKY/USDT P12_100

**Symbol:** SKY/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6453 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -3.5177 |
| sortino_ratio | -1.2317 |
| max_drawdown | 0.7506 |
| cagr | -0.4483 |
| net_avg_win | 52.0684 |
| net_avg_loss | -75.4726 |
| avg_hold_time_bars | 20.3261 |
| exposure | 0.5769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
