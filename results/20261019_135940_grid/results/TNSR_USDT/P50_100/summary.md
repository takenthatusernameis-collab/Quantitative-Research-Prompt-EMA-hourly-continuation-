# EMA Hourly Continuation — TNSR/USDT P50_100

**Symbol:** TNSR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.6197 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -4.3336 |
| sortino_ratio | -1.5364 |
| max_drawdown | 0.8475 |
| cagr | -0.5219 |
| net_avg_win | 45.8670 |
| net_avg_loss | -65.8910 |
| avg_hold_time_bars | 6.2669 |
| exposure | 0.1807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
