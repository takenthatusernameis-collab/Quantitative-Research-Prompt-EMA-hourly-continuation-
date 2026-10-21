# EMA Hourly Continuation — WIF/USDT P50_55

**Symbol:** WIF/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 89 |
| net_profit_factor | 0.9089 |
| net_win_rate | 0.5393 |
| gross_profit_factor | 1.1630 |
| gross_win_rate | 0.5393 |
| sharpe_ratio | -0.2655 |
| sortino_ratio | -0.0362 |
| max_drawdown | 0.1299 |
| cagr | -0.0175 |
| net_avg_win | 90.1756 |
| net_avg_loss | -116.1561 |
| avg_hold_time_bars | 4.3371 |
| exposure | 0.0175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
