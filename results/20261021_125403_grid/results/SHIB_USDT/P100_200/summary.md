# EMA Hourly Continuation — SHIB/USDT P100_200

**Symbol:** SHIB/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.8004 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0759 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -1.0678 |
| sortino_ratio | -0.2458 |
| max_drawdown | 0.2875 |
| cagr | -0.1069 |
| net_avg_win | 74.5387 |
| net_avg_loss | -101.5197 |
| avg_hold_time_bars | 12.3020 |
| exposure | 0.1426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
