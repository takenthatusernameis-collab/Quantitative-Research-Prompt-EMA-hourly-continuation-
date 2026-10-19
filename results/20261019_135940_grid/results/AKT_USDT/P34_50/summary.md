# EMA Hourly Continuation — AKT/USDT P34_50

**Symbol:** AKT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.4453 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.9459 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -7.8228 |
| sortino_ratio | -3.2830 |
| max_drawdown | 0.9840 |
| cagr | -0.8058 |
| net_avg_win | 20.0400 |
| net_avg_loss | -36.7132 |
| avg_hold_time_bars | 2.8221 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
