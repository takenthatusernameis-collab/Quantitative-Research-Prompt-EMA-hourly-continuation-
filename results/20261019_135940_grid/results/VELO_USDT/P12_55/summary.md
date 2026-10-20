# EMA Hourly Continuation — VELO/USDT P12_55

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.6334 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -4.7885 |
| sortino_ratio | -2.2474 |
| max_drawdown | 0.9377 |
| cagr | -0.6588 |
| net_avg_win | 29.7936 |
| net_avg_loss | -44.4094 |
| avg_hold_time_bars | 6.7612 |
| exposure | 0.3424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
