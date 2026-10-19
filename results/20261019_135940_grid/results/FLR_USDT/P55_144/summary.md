# EMA Hourly Continuation — FLR/USDT P55_144

**Symbol:** FLR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.5312 |
| net_win_rate | 0.4473 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -5.3857 |
| sortino_ratio | -1.8890 |
| max_drawdown | 0.9008 |
| cagr | -0.5989 |
| net_avg_win | 36.9123 |
| net_avg_loss | -56.2441 |
| avg_hold_time_bars | 8.1994 |
| exposure | 0.2300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
