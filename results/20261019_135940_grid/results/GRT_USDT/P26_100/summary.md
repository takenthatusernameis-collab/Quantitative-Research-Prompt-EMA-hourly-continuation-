# EMA Hourly Continuation — GRT/USDT P26_100

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5763 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -4.4732 |
| sortino_ratio | -1.6262 |
| max_drawdown | 0.8678 |
| cagr | -0.5415 |
| net_avg_win | 37.6174 |
| net_avg_loss | -57.0230 |
| avg_hold_time_bars | 11.1709 |
| exposure | 0.3372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
