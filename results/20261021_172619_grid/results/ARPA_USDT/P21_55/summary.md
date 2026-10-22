# EMA Hourly Continuation — ARPA/USDT P21_55

**Symbol:** ARPA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.6861 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9642 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -3.5497 |
| sortino_ratio | -1.2626 |
| max_drawdown | 0.7788 |
| cagr | -0.4390 |
| net_avg_win | 56.8625 |
| net_avg_loss | -74.9918 |
| avg_hold_time_bars | 8.0483 |
| exposure | 0.2262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
