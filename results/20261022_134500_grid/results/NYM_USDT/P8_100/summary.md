# EMA Hourly Continuation — NYM/USDT P8_100

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.3977 |
| net_win_rate | 0.3766 |
| gross_profit_factor | 0.7096 |
| gross_win_rate | 0.3926 |
| sharpe_ratio | -7.9489 |
| sortino_ratio | -2.7740 |
| max_drawdown | 0.9736 |
| cagr | -0.7611 |
| net_avg_win | 27.3274 |
| net_avg_loss | -41.5105 |
| avg_hold_time_bars | 24.2212 |
| exposure | 0.6870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
