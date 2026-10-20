# EMA Hourly Continuation — AGLD/USDT P34_144

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.7353 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 1.0228 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -2.5961 |
| sortino_ratio | -0.8606 |
| max_drawdown | 0.6804 |
| cagr | -0.3277 |
| net_avg_win | 66.0589 |
| net_avg_loss | -85.9650 |
| avg_hold_time_bars | 15.8971 |
| exposure | 0.3914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
