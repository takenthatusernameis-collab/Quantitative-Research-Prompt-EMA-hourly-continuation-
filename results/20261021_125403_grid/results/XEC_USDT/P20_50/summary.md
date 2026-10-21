# EMA Hourly Continuation — XEC/USDT P20_50

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.6787 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9874 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -3.6380 |
| sortino_ratio | -1.3103 |
| max_drawdown | 0.7966 |
| cagr | -0.4513 |
| net_avg_win | 54.0167 |
| net_avg_loss | -73.7854 |
| avg_hold_time_bars | 7.9148 |
| exposure | 0.2271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
