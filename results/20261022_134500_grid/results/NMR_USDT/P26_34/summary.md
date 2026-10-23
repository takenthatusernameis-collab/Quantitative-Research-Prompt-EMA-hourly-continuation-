# EMA Hourly Continuation — NMR/USDT P26_34

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1147 |
| net_profit_factor | 0.3460 |
| net_win_rate | 0.3810 |
| gross_profit_factor | 0.8841 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -12.9051 |
| sortino_ratio | -6.2947 |
| max_drawdown | 0.9997 |
| cagr | -0.9626 |
| net_avg_win | 12.1039 |
| net_avg_loss | -21.5307 |
| avg_hold_time_bars | 2.4926 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
