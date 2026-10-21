# EMA Hourly Continuation — UNI/USDT P55_144

**Symbol:** UNI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.9059 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1228 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -0.4712 |
| sortino_ratio | -0.1173 |
| max_drawdown | 0.2404 |
| cagr | -0.0557 |
| net_avg_win | 81.6311 |
| net_avg_loss | -102.4291 |
| avg_hold_time_bars | 18.2458 |
| exposure | 0.2463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
