# EMA Hourly Continuation — EGLD/USDT P12_200

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7590 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0426 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.6051 |
| sortino_ratio | -0.4547 |
| max_drawdown | 0.5018 |
| cagr | -0.1939 |
| net_avg_win | 64.8448 |
| net_avg_loss | -88.0347 |
| avg_hold_time_bars | 39.8550 |
| exposure | 0.7246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
