# EMA Hourly Continuation — BICO/USDT P20_50

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.4933 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -6.0884 |
| sortino_ratio | -2.6157 |
| max_drawdown | 0.9568 |
| cagr | -0.7135 |
| net_avg_win | 22.2321 |
| net_avg_loss | -36.7352 |
| avg_hold_time_bars | 5.6056 |
| exposure | 0.2377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
