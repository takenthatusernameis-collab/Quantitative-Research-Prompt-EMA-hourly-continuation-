# EMA Hourly Continuation — WLD/USDT P50_144

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7344 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 0.9750 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.7923 |
| sortino_ratio | -0.5166 |
| max_drawdown | 0.4691 |
| cagr | -0.2157 |
| net_avg_win | 61.3065 |
| net_avg_loss | -83.0743 |
| avg_hold_time_bars | 15.1404 |
| exposure | 0.2842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
