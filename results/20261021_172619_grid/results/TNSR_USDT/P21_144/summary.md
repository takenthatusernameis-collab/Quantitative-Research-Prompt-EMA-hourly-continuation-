# EMA Hourly Continuation — TNSR/USDT P21_144

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7604 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -1.8450 |
| sortino_ratio | -0.5204 |
| max_drawdown | 0.4867 |
| cagr | -0.2147 |
| net_avg_win | 76.6363 |
| net_avg_loss | -92.0241 |
| avg_hold_time_bars | 29.8157 |
| exposure | 0.5343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
