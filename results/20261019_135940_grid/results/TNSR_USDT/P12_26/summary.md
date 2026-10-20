# EMA Hourly Continuation — TNSR/USDT P12_26

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1380 |
| net_profit_factor | 0.5921 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 1.0129 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -8.7779 |
| sortino_ratio | -4.5958 |
| max_drawdown | 0.9966 |
| cagr | -0.8942 |
| net_avg_win | 23.5937 |
| net_avg_loss | -31.8491 |
| avg_hold_time_bars | 3.0804 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
