# EMA Hourly Continuation — TNSR/USDT P26_34

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1066 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -9.7975 |
| sortino_ratio | -4.5291 |
| max_drawdown | 0.9971 |
| cagr | -0.9006 |
| net_avg_win | 22.1996 |
| net_avg_loss | -33.2126 |
| avg_hold_time_bars | 2.2964 |
| exposure | 0.1108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
