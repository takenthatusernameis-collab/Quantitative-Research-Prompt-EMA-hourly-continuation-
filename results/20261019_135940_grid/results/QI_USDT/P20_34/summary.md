# EMA Hourly Continuation — QI/USDT P20_34

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.3768 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.8110 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -9.3649 |
| sortino_ratio | -4.2623 |
| max_drawdown | 0.9950 |
| cagr | -0.8774 |
| net_avg_win | 13.9894 |
| net_avg_loss | -26.6088 |
| avg_hold_time_bars | 3.2845 |
| exposure | 0.1531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
