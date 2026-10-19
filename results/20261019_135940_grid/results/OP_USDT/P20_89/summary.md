# EMA Hourly Continuation — OP/USDT P20_89

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.5902 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9090 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -4.2145 |
| sortino_ratio | -1.5508 |
| max_drawdown | 0.8514 |
| cagr | -0.5215 |
| net_avg_win | 37.9375 |
| net_avg_loss | -56.9797 |
| avg_hold_time_bars | 12.9809 |
| exposure | 0.4018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
