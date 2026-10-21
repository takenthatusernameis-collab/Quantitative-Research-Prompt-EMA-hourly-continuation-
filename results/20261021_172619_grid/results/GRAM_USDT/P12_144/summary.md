# EMA Hourly Continuation — GRAM/USDT P12_144

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.6070 |
| sortino_ratio | -0.4320 |
| max_drawdown | 0.4359 |
| cagr | -0.1805 |
| net_avg_win | 68.1678 |
| net_avg_loss | -87.7565 |
| avg_hold_time_bars | 39.8644 |
| exposure | 0.6415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
