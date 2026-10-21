# EMA Hourly Continuation — DCR/USDT P26_100

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.6125 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8043 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -3.3052 |
| sortino_ratio | -1.0677 |
| max_drawdown | 0.7248 |
| cagr | -0.3893 |
| net_avg_win | 47.8758 |
| net_avg_loss | -64.4520 |
| avg_hold_time_bars | 13.5519 |
| exposure | 0.3189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
