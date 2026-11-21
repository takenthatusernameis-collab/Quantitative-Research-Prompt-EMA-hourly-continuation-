# EMA Hourly Continuation — HTR/USDT P12_89

**Symbol:** HTR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.4917 |
| net_win_rate | 0.3912 |
| gross_profit_factor | 0.7183 |
| gross_win_rate | 0.4025 |
| sharpe_ratio | -7.4554 |
| sortino_ratio | -3.0955 |
| max_drawdown | 0.9780 |
| cagr | -0.7804 |
| net_avg_win | 27.2555 |
| net_avg_loss | -35.6215 |
| avg_hold_time_bars | 11.3145 |
| exposure | 0.4562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
