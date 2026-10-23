# EMA Hourly Continuation — COTI/USDT P21_50

**Symbol:** COTI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.5735 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.9382 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -7.0346 |
| sortino_ratio | -3.2316 |
| max_drawdown | 0.9800 |
| cagr | -0.7875 |
| net_avg_win | 27.7896 |
| net_avg_loss | -39.6678 |
| avg_hold_time_bars | 4.1709 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
