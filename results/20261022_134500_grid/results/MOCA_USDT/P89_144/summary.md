# EMA Hourly Continuation — MOCA/USDT P89_144

**Symbol:** MOCA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.4551 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.7837 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -5.7762 |
| sortino_ratio | -1.7593 |
| max_drawdown | 0.8635 |
| cagr | -0.5830 |
| net_avg_win | 41.4450 |
| net_avg_loss | -64.1560 |
| avg_hold_time_bars | 5.6057 |
| exposure | 0.1183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
