# EMA Hourly Continuation — CYBER/USDT P21_89

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.5824 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8797 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -4.5996 |
| sortino_ratio | -1.7388 |
| max_drawdown | 0.8824 |
| cagr | -0.5632 |
| net_avg_win | 36.8745 |
| net_avg_loss | -53.3229 |
| avg_hold_time_bars | 11.6436 |
| exposure | 0.3832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
