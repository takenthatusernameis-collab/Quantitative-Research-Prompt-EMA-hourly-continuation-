# EMA Hourly Continuation — SUN/USDT P55_100

**Symbol:** SUN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.2631 |
| net_win_rate | 0.3422 |
| gross_profit_factor | 0.6966 |
| gross_win_rate | 0.4100 |
| sharpe_ratio | -9.7557 |
| sortino_ratio | -3.3402 |
| max_drawdown | 0.9891 |
| cagr | -0.8330 |
| net_avg_win | 18.3895 |
| net_avg_loss | -36.3720 |
| avg_hold_time_bars | 6.6702 |
| exposure | 0.1693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
