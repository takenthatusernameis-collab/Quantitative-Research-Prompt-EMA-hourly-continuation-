# EMA Hourly Continuation — ENS/USDT P8_34

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1431 |
| net_profit_factor | 0.4893 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.8591 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -9.5532 |
| sortino_ratio | -5.0644 |
| max_drawdown | 0.9983 |
| cagr | -0.9209 |
| net_avg_win | 15.3261 |
| net_avg_loss | -24.2210 |
| avg_hold_time_bars | 5.4619 |
| exposure | 0.3553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
