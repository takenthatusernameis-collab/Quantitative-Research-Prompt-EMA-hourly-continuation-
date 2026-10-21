# EMA Hourly Continuation — WAVES/USDT P26_100

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6974 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9341 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -2.7589 |
| sortino_ratio | -0.8830 |
| max_drawdown | 0.6574 |
| cagr | -0.3341 |
| net_avg_win | 61.4317 |
| net_avg_loss | -80.3861 |
| avg_hold_time_bars | 13.9324 |
| exposure | 0.3185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
