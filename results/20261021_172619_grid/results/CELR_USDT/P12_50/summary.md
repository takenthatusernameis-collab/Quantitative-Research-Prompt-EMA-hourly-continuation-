# EMA Hourly Continuation — CELR/USDT P12_50

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.6883 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -3.5478 |
| sortino_ratio | -1.3507 |
| max_drawdown | 0.8008 |
| cagr | -0.4623 |
| net_avg_win | 52.4424 |
| net_avg_loss | -65.9024 |
| avg_hold_time_bars | 10.4387 |
| exposure | 0.3392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
