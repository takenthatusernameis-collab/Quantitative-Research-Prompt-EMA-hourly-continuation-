# EMA Hourly Continuation — TURBO/USDT P12_89

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.8375 |
| sortino_ratio | -1.4968 |
| max_drawdown | 0.7917 |
| cagr | -0.5109 |
| net_avg_win | 55.6904 |
| net_avg_loss | -73.5969 |
| avg_hold_time_bars | 14.7978 |
| exposure | 0.5191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
