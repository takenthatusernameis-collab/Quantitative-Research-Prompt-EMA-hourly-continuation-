# EMA Hourly Continuation — DEEP/USDT P21_34

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.8636 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1332 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.7898 |
| sortino_ratio | -0.2041 |
| max_drawdown | 0.2300 |
| cagr | -0.0913 |
| net_avg_win | 81.1492 |
| net_avg_loss | -107.2741 |
| avg_hold_time_bars | 4.9066 |
| exposure | 0.0714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
