# EMA Hourly Continuation — DBR/USDT P50_89

**Symbol:** DBR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.5671 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -3.3566 |
| sortino_ratio | -0.8586 |
| max_drawdown | 0.5691 |
| cagr | -0.3274 |
| net_avg_win | 61.4764 |
| net_avg_loss | -89.9458 |
| avg_hold_time_bars | 9.7752 |
| exposure | 0.1434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
