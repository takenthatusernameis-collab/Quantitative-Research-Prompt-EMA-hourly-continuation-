# EMA Hourly Continuation — ONDO/USDT P12_50

**Symbol:** ONDO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.8206 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.6142 |
| sortino_ratio | -0.5661 |
| max_drawdown | 0.5321 |
| cagr | -0.2302 |
| net_avg_win | 73.2242 |
| net_avg_loss | -90.4288 |
| avg_hold_time_bars | 10.3863 |
| exposure | 0.2823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
