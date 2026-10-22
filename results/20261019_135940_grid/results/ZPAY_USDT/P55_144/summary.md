# EMA Hourly Continuation — ZPAY/USDT P55_144

**Symbol:** ZPAY/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.4562 |
| net_win_rate | 0.3625 |
| gross_profit_factor | 0.6021 |
| gross_win_rate | 0.3645 |
| sharpe_ratio | -5.4348 |
| sortino_ratio | -1.7024 |
| max_drawdown | 0.8664 |
| cagr | -0.5480 |
| net_avg_win | 39.8746 |
| net_avg_loss | -49.7126 |
| avg_hold_time_bars | 16.6534 |
| exposure | 0.3783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
