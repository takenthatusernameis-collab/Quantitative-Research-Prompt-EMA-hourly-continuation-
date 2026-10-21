# EMA Hourly Continuation — SNX/USDT P12_21

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7577 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0901 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -1.7681 |
| sortino_ratio | -0.4917 |
| max_drawdown | 0.4858 |
| cagr | -0.2000 |
| net_avg_win | 69.7689 |
| net_avg_loss | -98.7238 |
| avg_hold_time_bars | 4.9464 |
| exposure | 0.0835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
