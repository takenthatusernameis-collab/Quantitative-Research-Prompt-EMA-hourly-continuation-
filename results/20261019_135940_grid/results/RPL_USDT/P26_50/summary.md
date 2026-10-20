# EMA Hourly Continuation — RPL/USDT P26_50

**Symbol:** RPL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.5476 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 1.0065 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -6.1367 |
| sortino_ratio | -2.5867 |
| max_drawdown | 0.9589 |
| cagr | -0.7150 |
| net_avg_win | 27.6737 |
| net_avg_loss | -44.1116 |
| avg_hold_time_bars | 4.9466 |
| exposure | 0.2012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
