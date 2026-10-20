# EMA Hourly Continuation — SWFTC/USDT P12_50

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.4406 |
| net_win_rate | 0.4036 |
| gross_profit_factor | 0.7478 |
| gross_win_rate | 0.4187 |
| sharpe_ratio | -8.9040 |
| sortino_ratio | -4.0631 |
| max_drawdown | 0.9938 |
| cagr | -0.8679 |
| net_avg_win | 18.3347 |
| net_avg_loss | -28.1569 |
| avg_hold_time_bars | 6.8223 |
| exposure | 0.3281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
