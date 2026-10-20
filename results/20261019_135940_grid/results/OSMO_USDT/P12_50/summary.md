# EMA Hourly Continuation — OSMO/USDT P12_50

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1066 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.9821 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -7.8304 |
| sortino_ratio | -3.6016 |
| max_drawdown | 0.9878 |
| cagr | -0.8259 |
| net_avg_win | 29.0591 |
| net_avg_loss | -38.1333 |
| avg_hold_time_bars | 7.4287 |
| exposure | 0.3600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
