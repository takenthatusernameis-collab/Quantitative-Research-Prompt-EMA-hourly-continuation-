# EMA Hourly Continuation — SSV/USDT P89_144

**Symbol:** SSV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6809 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -1.9543 |
| sortino_ratio | -0.4810 |
| max_drawdown | 0.4412 |
| cagr | -0.1978 |
| net_avg_win | 63.6430 |
| net_avg_loss | -86.2279 |
| avg_hold_time_bars | 7.1846 |
| exposure | 0.0969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
