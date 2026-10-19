# EMA Hourly Continuation — CVX/USDT P55_89

**Symbol:** CVX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.4927 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8599 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -5.4064 |
| sortino_ratio | -1.9238 |
| max_drawdown | 0.9068 |
| cagr | -0.6113 |
| net_avg_win | 30.2620 |
| net_avg_loss | -51.0696 |
| avg_hold_time_bars | 4.5835 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
