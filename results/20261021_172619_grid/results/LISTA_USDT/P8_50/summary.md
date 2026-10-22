# EMA Hourly Continuation — LISTA/USDT P8_50

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.7231 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8927 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -2.8383 |
| sortino_ratio | -1.0801 |
| max_drawdown | 0.7127 |
| cagr | -0.3919 |
| net_avg_win | 57.1362 |
| net_avg_loss | -70.4829 |
| avg_hold_time_bars | 13.7883 |
| exposure | 0.4490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
