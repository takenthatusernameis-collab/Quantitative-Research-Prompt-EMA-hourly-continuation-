# EMA Hourly Continuation — TNSR/USDT P26_89

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.7353 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0386 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -2.9627 |
| sortino_ratio | -1.1118 |
| max_drawdown | 0.7580 |
| cagr | -0.4097 |
| net_avg_win | 57.7206 |
| net_avg_loss | -78.4949 |
| avg_hold_time_bars | 9.5904 |
| exposure | 0.3073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
