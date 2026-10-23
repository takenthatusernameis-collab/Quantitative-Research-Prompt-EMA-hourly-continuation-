# EMA Hourly Continuation — FLOW/USDT P20_50

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.4435 |
| net_win_rate | 0.4335 |
| gross_profit_factor | 0.8498 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -8.1980 |
| sortino_ratio | -3.6750 |
| max_drawdown | 0.9897 |
| cagr | -0.8365 |
| net_avg_win | 18.0445 |
| net_avg_loss | -31.1375 |
| avg_hold_time_bars | 4.8363 |
| exposure | 0.2216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
