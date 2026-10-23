# EMA Hourly Continuation — NOT/USDT P20_50

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.5395 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -6.7129 |
| sortino_ratio | -3.1036 |
| max_drawdown | 0.9770 |
| cagr | -0.7811 |
| net_avg_win | 23.6002 |
| net_avg_loss | -37.6745 |
| avg_hold_time_bars | 4.1300 |
| exposure | 0.2029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
