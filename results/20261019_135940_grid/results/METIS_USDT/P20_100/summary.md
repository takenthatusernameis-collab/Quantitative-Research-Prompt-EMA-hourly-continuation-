# EMA Hourly Continuation — METIS/USDT P20_100

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.5414 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.8036 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -5.5409 |
| sortino_ratio | -2.0314 |
| max_drawdown | 0.9152 |
| cagr | -0.6229 |
| net_avg_win | 37.3254 |
| net_avg_loss | -50.8244 |
| avg_hold_time_bars | 13.0954 |
| exposure | 0.4054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
