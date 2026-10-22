# EMA Hourly Continuation — CYBER/USDT P55_144

**Symbol:** CYBER/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.8051 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0341 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -1.1886 |
| sortino_ratio | -0.3317 |
| max_drawdown | 0.3706 |
| cagr | -0.1422 |
| net_avg_win | 68.0829 |
| net_avg_loss | -89.6487 |
| avg_hold_time_bars | 15.1247 |
| exposure | 0.2592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
