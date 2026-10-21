# EMA Hourly Continuation — GLM/USDT P55_200

**Symbol:** GLM/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0007 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.4817 |
| sortino_ratio | -0.3910 |
| max_drawdown | 0.4048 |
| cagr | -0.1658 |
| net_avg_win | 68.3198 |
| net_avg_loss | -91.1736 |
| avg_hold_time_bars | 22.8270 |
| exposure | 0.3538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
