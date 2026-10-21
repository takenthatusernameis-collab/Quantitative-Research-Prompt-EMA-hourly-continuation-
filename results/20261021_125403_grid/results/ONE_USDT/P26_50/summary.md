# EMA Hourly Continuation — ONE/USDT P26_50

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8052 |
| net_win_rate | 0.5137 |
| gross_profit_factor | 1.0577 |
| gross_win_rate | 0.5137 |
| sharpe_ratio | -1.3819 |
| sortino_ratio | -0.3983 |
| max_drawdown | 0.4168 |
| cagr | -0.1676 |
| net_avg_win | 74.0575 |
| net_avg_loss | -97.1612 |
| avg_hold_time_bars | 8.1397 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
