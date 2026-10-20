# EMA Hourly Continuation — RLC/USDT P26_144

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.6770 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -2.9940 |
| sortino_ratio | -1.0275 |
| max_drawdown | 0.7246 |
| cagr | -0.3835 |
| net_avg_win | 51.0068 |
| net_avg_loss | -73.0640 |
| avg_hold_time_bars | 16.3032 |
| exposure | 0.4350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
