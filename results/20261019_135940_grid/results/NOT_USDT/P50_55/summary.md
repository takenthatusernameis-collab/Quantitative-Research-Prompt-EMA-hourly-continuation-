# EMA Hourly Continuation — NOT/USDT P50_55

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.2741 |
| net_win_rate | 0.3617 |
| gross_profit_factor | 0.7176 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -12.1344 |
| sortino_ratio | -5.1173 |
| max_drawdown | 0.9989 |
| cagr | -0.9388 |
| net_avg_win | 12.8720 |
| net_avg_loss | -26.6155 |
| avg_hold_time_bars | 1.7716 |
| exposure | 0.0674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
