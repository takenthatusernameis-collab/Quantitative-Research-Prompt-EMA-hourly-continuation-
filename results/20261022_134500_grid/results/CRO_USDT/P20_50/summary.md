# EMA Hourly Continuation — CRO/USDT P20_50

**Symbol:** CRO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1031 |
| net_profit_factor | 0.3504 |
| net_win_rate | 0.4025 |
| gross_profit_factor | 0.8182 |
| gross_win_rate | 0.4345 |
| sharpe_ratio | -10.3920 |
| sortino_ratio | -4.7184 |
| max_drawdown | 0.9978 |
| cagr | -0.9110 |
| net_avg_win | 12.9706 |
| net_avg_loss | -24.9348 |
| avg_hold_time_bars | 4.9845 |
| exposure | 0.2336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
