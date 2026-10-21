# EMA Hourly Continuation — AAVE/USDT P50_55

**Symbol:** AAVE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 92 |
| net_profit_factor | 0.8610 |
| net_win_rate | 0.5435 |
| gross_profit_factor | 1.1802 |
| gross_win_rate | 0.5435 |
| sharpe_ratio | -0.4185 |
| sortino_ratio | -0.0582 |
| max_drawdown | 0.0909 |
| cagr | -0.0267 |
| net_avg_win | 81.4863 |
| net_avg_loss | -112.6727 |
| avg_hold_time_bars | 4.8913 |
| exposure | 0.0205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
