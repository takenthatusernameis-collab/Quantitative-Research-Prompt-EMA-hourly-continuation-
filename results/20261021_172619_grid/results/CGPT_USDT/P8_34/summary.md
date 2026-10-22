# EMA Hourly Continuation — CGPT/USDT P8_34

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.8936 |
| net_win_rate | 0.5328 |
| gross_profit_factor | 1.1372 |
| gross_win_rate | 0.5328 |
| sharpe_ratio | -0.9822 |
| sortino_ratio | -0.3799 |
| max_drawdown | 0.4307 |
| cagr | -0.1654 |
| net_avg_win | 80.2008 |
| net_avg_loss | -102.3453 |
| avg_hold_time_bars | 8.6360 |
| exposure | 0.2815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
