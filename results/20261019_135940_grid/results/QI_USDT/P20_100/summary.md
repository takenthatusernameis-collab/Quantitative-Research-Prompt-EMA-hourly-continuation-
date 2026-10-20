# EMA Hourly Continuation — QI/USDT P20_100

**Symbol:** QI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6460 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9884 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -3.3493 |
| sortino_ratio | -1.1564 |
| max_drawdown | 0.7546 |
| cagr | -0.4227 |
| net_avg_win | 46.3919 |
| net_avg_loss | -69.0058 |
| avg_hold_time_bars | 15.5465 |
| exposure | 0.4235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
