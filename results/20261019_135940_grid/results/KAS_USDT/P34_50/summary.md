# EMA Hourly Continuation — KAS/USDT P34_50

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.2092 |
| net_win_rate | 0.3930 |
| gross_profit_factor | 0.5442 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -10.8943 |
| sortino_ratio | -4.7240 |
| max_drawdown | 0.9979 |
| cagr | -0.9129 |
| net_avg_win | 7.3744 |
| net_avg_loss | -22.8178 |
| avg_hold_time_bars | 2.4929 |
| exposure | 0.1032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
