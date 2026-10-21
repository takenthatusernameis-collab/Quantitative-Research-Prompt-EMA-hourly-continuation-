# EMA Hourly Continuation — UQC/USDT P50_55

**Symbol:** UQC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.1589 |
| net_win_rate | 0.1584 |
| gross_profit_factor | 0.2894 |
| gross_win_rate | 0.2081 |
| sharpe_ratio | -8.5147 |
| sortino_ratio | -1.9169 |
| max_drawdown | 0.9329 |
| cagr | -0.6562 |
| net_avg_win | 50.3349 |
| net_avg_loss | -59.5956 |
| avg_hold_time_bars | 16.6199 |
| exposure | 0.1662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
