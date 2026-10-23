# EMA Hourly Continuation — SSV/USDT P50_89

**Symbol:** SSV/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 759 |
| net_profit_factor | 0.4642 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.7959 |
| gross_win_rate | 0.4506 |
| sharpe_ratio | -6.6089 |
| sortino_ratio | -2.5532 |
| max_drawdown | 0.9595 |
| cagr | -0.7138 |
| net_avg_win | 25.2845 |
| net_avg_loss | -41.4553 |
| avg_hold_time_bars | 4.6271 |
| exposure | 0.1589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
