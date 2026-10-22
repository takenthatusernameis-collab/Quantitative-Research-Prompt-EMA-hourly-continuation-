# EMA Hourly Continuation — JST/USDT P8_12

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1510 |
| net_profit_factor | 0.0947 |
| net_win_rate | 0.2815 |
| gross_profit_factor | 0.6564 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -20.8354 |
| sortino_ratio | -12.5888 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 2.4608 |
| net_avg_loss | -10.1805 |
| avg_hold_time_bars | 2.4152 |
| exposure | 0.1650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
