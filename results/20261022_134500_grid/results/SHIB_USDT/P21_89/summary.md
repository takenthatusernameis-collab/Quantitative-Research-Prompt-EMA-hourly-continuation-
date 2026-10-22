# EMA Hourly Continuation — SHIB/USDT P21_89

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.5510 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -5.6538 |
| sortino_ratio | -2.1714 |
| max_drawdown | 0.9316 |
| cagr | -0.6518 |
| net_avg_win | 33.7438 |
| net_avg_loss | -50.6073 |
| avg_hold_time_bars | 9.7390 |
| exposure | 0.3307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
