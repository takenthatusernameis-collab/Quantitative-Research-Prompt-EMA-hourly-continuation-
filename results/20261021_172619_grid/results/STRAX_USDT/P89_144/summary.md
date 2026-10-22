# EMA Hourly Continuation — STRAX/USDT P89_144

**Symbol:** STRAX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.5057 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.7371 |
| gross_win_rate | 0.4217 |
| sharpe_ratio | -3.9851 |
| sortino_ratio | -1.0347 |
| max_drawdown | 0.6990 |
| cagr | -0.3818 |
| net_avg_win | 51.0807 |
| net_avg_loss | -73.6526 |
| avg_hold_time_bars | 8.8464 |
| exposure | 0.1343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
