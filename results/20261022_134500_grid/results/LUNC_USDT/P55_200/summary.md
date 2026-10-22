# EMA Hourly Continuation — LUNC/USDT P55_200

**Symbol:** LUNC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.6568 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0224 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -2.7820 |
| sortino_ratio | -0.8067 |
| max_drawdown | 0.6391 |
| cagr | -0.3235 |
| net_avg_win | 55.9235 |
| net_avg_loss | -85.5403 |
| avg_hold_time_bars | 18.4215 |
| exposure | 0.3575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
