# EMA Hourly Continuation — RLC/USDT P89_100

**Symbol:** RLC/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.2782 |
| net_win_rate | 0.3862 |
| gross_profit_factor | 0.7719 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -9.3929 |
| sortino_ratio | -3.4661 |
| max_drawdown | 0.9893 |
| cagr | -0.8347 |
| net_avg_win | 15.1920 |
| net_avg_loss | -34.3468 |
| avg_hold_time_bars | 2.3062 |
| exposure | 0.0681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
