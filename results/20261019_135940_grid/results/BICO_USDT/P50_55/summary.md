# EMA Hourly Continuation — BICO/USDT P50_55

**Symbol:** BICO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.2755 |
| net_win_rate | 0.4055 |
| gross_profit_factor | 0.8084 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -9.5428 |
| sortino_ratio | -3.8347 |
| max_drawdown | 0.9929 |
| cagr | -0.8601 |
| net_avg_win | 11.7273 |
| net_avg_loss | -29.0351 |
| avg_hold_time_bars | 2.7645 |
| exposure | 0.0998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
