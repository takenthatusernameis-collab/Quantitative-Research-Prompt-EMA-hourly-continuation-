# EMA Hourly Continuation — QI/USDT P26_200

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.6239 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9288 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.9985 |
| sortino_ratio | -0.8797 |
| max_drawdown | 0.6687 |
| cagr | -0.3423 |
| net_avg_win | 52.2845 |
| net_avg_loss | -75.7571 |
| avg_hold_time_bars | 25.3922 |
| exposure | 0.5010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
