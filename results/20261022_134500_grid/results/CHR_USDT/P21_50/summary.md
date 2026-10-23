# EMA Hourly Continuation — CHR/USDT P21_50

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.5041 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -7.0519 |
| sortino_ratio | -3.1385 |
| max_drawdown | 0.9785 |
| cagr | -0.7792 |
| net_avg_win | 22.6928 |
| net_avg_loss | -35.1479 |
| avg_hold_time_bars | 4.8789 |
| exposure | 0.2206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
