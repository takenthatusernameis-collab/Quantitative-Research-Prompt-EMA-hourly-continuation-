# EMA Hourly Continuation — GMT/USDT P26_34

**Symbol:** GMT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.6571 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9269 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -1.7942 |
| sortino_ratio | -0.3556 |
| max_drawdown | 0.3448 |
| cagr | -0.1500 |
| net_avg_win | 69.8102 |
| net_avg_loss | -98.7245 |
| avg_hold_time_bars | 5.1623 |
| exposure | 0.0448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
