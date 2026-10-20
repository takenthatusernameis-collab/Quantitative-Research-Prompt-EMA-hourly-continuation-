# EMA Hourly Continuation — SATS/USDT P21_144

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6138 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8582 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -3.7201 |
| sortino_ratio | -1.1912 |
| max_drawdown | 0.7662 |
| cagr | -0.4285 |
| net_avg_win | 52.4826 |
| net_avg_loss | -67.5174 |
| avg_hold_time_bars | 20.5106 |
| exposure | 0.4817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
