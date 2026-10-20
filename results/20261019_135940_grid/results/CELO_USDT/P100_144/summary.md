# EMA Hourly Continuation — CELO/USDT P100_144

**Symbol:** CELO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.5008 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -4.8734 |
| sortino_ratio | -1.4714 |
| max_drawdown | 0.8424 |
| cagr | -0.5126 |
| net_avg_win | 40.5599 |
| net_avg_loss | -66.5256 |
| avg_hold_time_bars | 4.4270 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
