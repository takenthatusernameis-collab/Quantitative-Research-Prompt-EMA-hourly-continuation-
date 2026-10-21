# EMA Hourly Continuation — STRAX/USDT P100_200

**Symbol:** STRAX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.4613 |
| net_win_rate | 0.3958 |
| gross_profit_factor | 0.6295 |
| gross_win_rate | 0.3958 |
| sharpe_ratio | -4.2392 |
| sortino_ratio | -1.1021 |
| max_drawdown | 0.7275 |
| cagr | -0.4016 |
| net_avg_win | 46.5084 |
| net_avg_loss | -66.0608 |
| avg_hold_time_bars | 11.7083 |
| exposure | 0.1799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
