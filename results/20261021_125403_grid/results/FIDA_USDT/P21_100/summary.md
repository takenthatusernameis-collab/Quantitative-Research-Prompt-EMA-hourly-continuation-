# EMA Hourly Continuation — FIDA/USDT P21_100

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6744 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.3917 |
| sortino_ratio | -0.7477 |
| max_drawdown | 0.6057 |
| cagr | -0.2911 |
| net_avg_win | 52.2408 |
| net_avg_loss | -70.1477 |
| avg_hold_time_bars | 19.7975 |
| exposure | 0.4336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
