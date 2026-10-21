# EMA Hourly Continuation — BRETT/USDT P8_144

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8902 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.0008 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -0.5658 |
| sortino_ratio | -0.1464 |
| max_drawdown | 0.2395 |
| cagr | -0.0686 |
| net_avg_win | 81.0873 |
| net_avg_loss | -92.2840 |
| avg_hold_time_bars | 52.5649 |
| exposure | 0.7790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
