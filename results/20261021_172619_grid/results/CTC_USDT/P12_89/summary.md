# EMA Hourly Continuation — CTC/USDT P12_89

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.8107 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0565 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -1.5219 |
| sortino_ratio | -0.5109 |
| max_drawdown | 0.5134 |
| cagr | -0.2118 |
| net_avg_win | 68.3388 |
| net_avg_loss | -89.7028 |
| avg_hold_time_bars | 21.1353 |
| exposure | 0.5255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
