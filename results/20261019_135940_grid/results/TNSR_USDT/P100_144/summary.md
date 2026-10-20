# EMA Hourly Continuation — TNSR/USDT P100_144

**Symbol:** TNSR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.9419 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -3.9757 |
| sortino_ratio | -1.2561 |
| max_drawdown | 0.7758 |
| cagr | -0.4453 |
| net_avg_win | 43.9786 |
| net_avg_loss | -68.3096 |
| avg_hold_time_bars | 4.4949 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
