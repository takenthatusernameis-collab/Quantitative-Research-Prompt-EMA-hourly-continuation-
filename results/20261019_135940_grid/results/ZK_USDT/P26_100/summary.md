# EMA Hourly Continuation — ZK/USDT P26_100

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -3.4964 |
| sortino_ratio | -1.2965 |
| max_drawdown | 0.7698 |
| cagr | -0.4620 |
| net_avg_win | 53.0308 |
| net_avg_loss | -72.7234 |
| avg_hold_time_bars | 10.8508 |
| exposure | 0.3439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
