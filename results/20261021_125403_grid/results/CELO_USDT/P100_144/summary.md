# EMA Hourly Continuation — CELO/USDT P100_144

**Symbol:** CELO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7513 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0603 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.4957 |
| sortino_ratio | -0.3397 |
| max_drawdown | 0.3978 |
| cagr | -0.1441 |
| net_avg_win | 76.5952 |
| net_avg_loss | -106.9702 |
| avg_hold_time_bars | 6.8680 |
| exposure | 0.0777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
