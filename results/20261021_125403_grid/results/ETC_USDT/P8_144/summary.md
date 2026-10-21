# EMA Hourly Continuation — ETC/USDT P8_144

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9113 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.0410 |
| sortino_ratio | -0.5521 |
| max_drawdown | 0.5289 |
| cagr | -0.2240 |
| net_avg_win | 63.6701 |
| net_avg_loss | -84.0927 |
| avg_hold_time_bars | 45.4694 |
| exposure | 0.7440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
