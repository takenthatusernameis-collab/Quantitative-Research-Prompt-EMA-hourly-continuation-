# EMA Hourly Continuation — INJ/USDT P34_100

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.8243 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0083 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3210 |
| sortino_ratio | -0.3860 |
| max_drawdown | 0.4224 |
| cagr | -0.1640 |
| net_avg_win | 81.7410 |
| net_avg_loss | -99.1582 |
| avg_hold_time_bars | 12.4543 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
