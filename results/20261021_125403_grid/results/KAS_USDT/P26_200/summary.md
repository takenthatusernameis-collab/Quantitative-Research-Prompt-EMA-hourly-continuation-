# EMA Hourly Continuation — KAS/USDT P26_200

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.7650 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.4410 |
| sortino_ratio | -0.3792 |
| max_drawdown | 0.3791 |
| cagr | -0.1608 |
| net_avg_win | 69.8158 |
| net_avg_loss | -86.5734 |
| avg_hold_time_bars | 30.0616 |
| exposure | 0.4660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
