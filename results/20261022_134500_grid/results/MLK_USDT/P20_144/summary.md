# EMA Hourly Continuation — MLK/USDT P20_144

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 790 |
| net_profit_factor | 0.3654 |
| net_win_rate | 0.3329 |
| gross_profit_factor | 0.6009 |
| gross_win_rate | 0.3354 |
| sharpe_ratio | -9.6034 |
| sortino_ratio | -3.8042 |
| max_drawdown | 0.9916 |
| cagr | -0.8484 |
| net_avg_win | 21.7092 |
| net_avg_loss | -29.6465 |
| avg_hold_time_bars | 13.7367 |
| exposure | 0.4911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
