# EMA Hourly Continuation — CHR/USDT P55_100

**Symbol:** CHR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.5286 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8300 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -5.3316 |
| sortino_ratio | -1.9834 |
| max_drawdown | 0.9127 |
| cagr | -0.6093 |
| net_avg_win | 32.6879 |
| net_avg_loss | -50.7439 |
| avg_hold_time_bars | 5.1580 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
