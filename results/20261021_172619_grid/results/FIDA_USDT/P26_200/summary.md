# EMA Hourly Continuation — FIDA/USDT P26_200

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.8143 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -1.1306 |
| sortino_ratio | -0.3073 |
| max_drawdown | 0.3355 |
| cagr | -0.1336 |
| net_avg_win | 72.7324 |
| net_avg_loss | -91.3106 |
| avg_hold_time_bars | 32.6713 |
| exposure | 0.5352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
