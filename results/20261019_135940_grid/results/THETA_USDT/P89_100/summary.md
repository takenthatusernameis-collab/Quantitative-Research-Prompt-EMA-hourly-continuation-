# EMA Hourly Continuation — THETA/USDT P89_100

**Symbol:** THETA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.2926 |
| net_win_rate | 0.4194 |
| gross_profit_factor | 0.8271 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -8.3434 |
| sortino_ratio | -2.9107 |
| max_drawdown | 0.9794 |
| cagr | -0.7853 |
| net_avg_win | 16.3980 |
| net_avg_loss | -40.4693 |
| avg_hold_time_bars | 1.9185 |
| exposure | 0.0514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
