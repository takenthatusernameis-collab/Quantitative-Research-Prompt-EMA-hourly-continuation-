# EMA Hourly Continuation — WIN/USDT P8_100

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.4964 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8751 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -5.2993 |
| sortino_ratio | -1.9209 |
| max_drawdown | 0.9109 |
| cagr | -0.6152 |
| net_avg_win | 29.2798 |
| net_avg_loss | -49.4546 |
| avg_hold_time_bars | 21.7168 |
| exposure | 0.6624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
