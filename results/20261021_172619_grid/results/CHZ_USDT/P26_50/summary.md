# EMA Hourly Continuation — CHZ/USDT P26_50

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6891 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9579 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.6119 |
| sortino_ratio | -0.7636 |
| max_drawdown | 0.5950 |
| cagr | -0.2950 |
| net_avg_win | 64.7614 |
| net_avg_loss | -86.6118 |
| avg_hold_time_bars | 6.6978 |
| exposure | 0.1270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
