# EMA Hourly Continuation — AGLD/USDT P89_100

**Symbol:** AGLD/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.3720 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.9105 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -7.6752 |
| sortino_ratio | -2.7350 |
| max_drawdown | 0.9691 |
| cagr | -0.7454 |
| net_avg_win | 22.1475 |
| net_avg_loss | -42.2442 |
| avg_hold_time_bars | 2.9087 |
| exposure | 0.0821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
