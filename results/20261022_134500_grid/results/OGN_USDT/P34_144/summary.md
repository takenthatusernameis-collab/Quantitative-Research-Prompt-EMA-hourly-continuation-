# EMA Hourly Continuation — OGN/USDT P34_144

**Symbol:** OGN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.5410 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -4.6482 |
| sortino_ratio | -1.4680 |
| max_drawdown | 0.8328 |
| cagr | -0.5024 |
| net_avg_win | 44.9702 |
| net_avg_loss | -62.8554 |
| avg_hold_time_bars | 18.4167 |
| exposure | 0.4200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
