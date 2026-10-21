# EMA Hourly Continuation — TAO/USDT P21_100

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.8915 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0521 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -0.7810 |
| sortino_ratio | -0.2385 |
| max_drawdown | 0.3495 |
| cagr | -0.1079 |
| net_avg_win | 88.3106 |
| net_avg_loss | -104.4628 |
| avg_hold_time_bars | 17.7611 |
| exposure | 0.3649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
