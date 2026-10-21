# EMA Hourly Continuation — GRAM/USDT P55_144

**Symbol:** GRAM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6671 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.8993 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.1718 |
| sortino_ratio | -0.5585 |
| max_drawdown | 0.4971 |
| cagr | -0.2264 |
| net_avg_win | 61.4282 |
| net_avg_loss | -84.4562 |
| avg_hold_time_bars | 14.8673 |
| exposure | 0.2190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
