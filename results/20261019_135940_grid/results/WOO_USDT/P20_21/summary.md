# EMA Hourly Continuation — WOO/USDT P20_21

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1185 |
| net_profit_factor | 0.1780 |
| net_win_rate | 0.3021 |
| gross_profit_factor | 0.7135 |
| gross_win_rate | 0.3848 |
| sharpe_ratio | -16.9636 |
| sortino_ratio | -8.7380 |
| max_drawdown | 1.0000 |
| cagr | -0.9922 |
| net_avg_win | 6.0481 |
| net_avg_loss | -14.7100 |
| avg_hold_time_bars | 1.8489 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
