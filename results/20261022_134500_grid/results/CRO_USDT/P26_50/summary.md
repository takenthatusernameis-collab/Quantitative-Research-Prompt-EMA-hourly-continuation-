# EMA Hourly Continuation — CRO/USDT P26_50

**Symbol:** CRO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.3131 |
| net_win_rate | 0.4073 |
| gross_profit_factor | 0.8153 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -10.3483 |
| sortino_ratio | -4.5799 |
| max_drawdown | 0.9973 |
| cagr | -0.9050 |
| net_avg_win | 11.5665 |
| net_avg_loss | -25.3820 |
| avg_hold_time_bars | 3.7648 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
