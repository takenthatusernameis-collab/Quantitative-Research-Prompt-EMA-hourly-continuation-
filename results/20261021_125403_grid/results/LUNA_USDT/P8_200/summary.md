# EMA Hourly Continuation — LUNA/USDT P8_200

**Symbol:** LUNA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8328 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0040 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.0375 |
| sortino_ratio | -0.2676 |
| max_drawdown | 0.3044 |
| cagr | -0.1179 |
| net_avg_win | 82.6126 |
| net_avg_loss | -99.8061 |
| avg_hold_time_bars | 50.6277 |
| exposure | 0.7479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
