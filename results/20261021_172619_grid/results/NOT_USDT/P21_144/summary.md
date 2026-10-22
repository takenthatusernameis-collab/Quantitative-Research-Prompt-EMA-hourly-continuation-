# EMA Hourly Continuation — NOT/USDT P21_144

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.8574 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -0.9189 |
| sortino_ratio | -0.2463 |
| max_drawdown | 0.3149 |
| cagr | -0.1093 |
| net_avg_win | 86.7281 |
| net_avg_loss | -101.7529 |
| avg_hold_time_bars | 33.5929 |
| exposure | 0.5349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
