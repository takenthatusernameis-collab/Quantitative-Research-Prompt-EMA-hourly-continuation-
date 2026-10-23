# EMA Hourly Continuation — ORDI/USDT P50_200

**Symbol:** ORDI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7118 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 1.0315 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -2.1472 |
| sortino_ratio | -0.6153 |
| max_drawdown | 0.5398 |
| cagr | -0.2531 |
| net_avg_win | 62.5846 |
| net_avg_loss | -86.2409 |
| avg_hold_time_bars | 20.1401 |
| exposure | 0.3790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
