# EMA Hourly Continuation — LUNA/USDT P89_144

**Symbol:** LUNA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.4105 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.8279 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -6.5898 |
| sortino_ratio | -2.2616 |
| max_drawdown | 0.9406 |
| cagr | -0.6722 |
| net_avg_win | 26.2697 |
| net_avg_loss | -47.5628 |
| avg_hold_time_bars | 4.8527 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
