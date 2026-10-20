# EMA Hourly Continuation — SYN/USDT P12_26

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1346 |
| net_profit_factor | 0.4403 |
| net_win_rate | 0.4220 |
| gross_profit_factor | 0.8177 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -9.5525 |
| sortino_ratio | -4.9158 |
| max_drawdown | 0.9979 |
| cagr | -0.9136 |
| net_avg_win | 13.8224 |
| net_avg_loss | -22.9175 |
| avg_hold_time_bars | 3.4235 |
| exposure | 0.2095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
