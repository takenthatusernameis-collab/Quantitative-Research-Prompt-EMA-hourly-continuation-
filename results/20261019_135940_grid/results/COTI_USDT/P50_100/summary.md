# EMA Hourly Continuation — COTI/USDT P50_100

**Symbol:** COTI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5402 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -4.3924 |
| sortino_ratio | -1.6013 |
| max_drawdown | 0.8556 |
| cagr | -0.5370 |
| net_avg_win | 31.5091 |
| net_avg_loss | -53.4634 |
| avg_hold_time_bars | 5.3988 |
| exposure | 0.1637 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
