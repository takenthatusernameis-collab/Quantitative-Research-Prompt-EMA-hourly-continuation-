# EMA Hourly Continuation — IOTA/USDT P21_144

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.6511 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9863 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -3.0597 |
| sortino_ratio | -0.9498 |
| max_drawdown | 0.6888 |
| cagr | -0.3619 |
| net_avg_win | 54.8906 |
| net_avg_loss | -76.6356 |
| avg_hold_time_bars | 23.9876 |
| exposure | 0.5266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
