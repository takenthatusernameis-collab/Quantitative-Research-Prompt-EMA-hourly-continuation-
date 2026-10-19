# EMA Hourly Continuation — WLD/USDT P8_144

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0966 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | -1.4495 |
| sortino_ratio | -0.4491 |
| max_drawdown | 0.4542 |
| cagr | -0.1985 |
| net_avg_win | 75.5086 |
| net_avg_loss | -99.3311 |
| avg_hold_time_bars | 33.0449 |
| exposure | 0.7360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
