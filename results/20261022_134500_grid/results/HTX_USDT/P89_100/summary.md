# EMA Hourly Continuation — HTX/USDT P89_100

**Symbol:** HTX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.0716 |
| net_win_rate | 0.1737 |
| gross_profit_factor | 0.3683 |
| gross_win_rate | 0.2865 |
| sharpe_ratio | -16.7761 |
| sortino_ratio | -7.4074 |
| max_drawdown | 1.0000 |
| cagr | -0.9847 |
| net_avg_win | 6.4290 |
| net_avg_loss | -18.8638 |
| avg_hold_time_bars | 2.5427 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
