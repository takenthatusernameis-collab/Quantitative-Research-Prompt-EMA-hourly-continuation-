# EMA Hourly Continuation — IMX/USDT P89_100

**Symbol:** IMX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.2745 |
| net_win_rate | 0.3887 |
| gross_profit_factor | 0.6575 |
| gross_win_rate | 0.4194 |
| sharpe_ratio | -9.1352 |
| sortino_ratio | -3.2797 |
| max_drawdown | 0.9863 |
| cagr | -0.8165 |
| net_avg_win | 15.4792 |
| net_avg_loss | -35.8620 |
| avg_hold_time_bars | 2.0355 |
| exposure | 0.0571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
