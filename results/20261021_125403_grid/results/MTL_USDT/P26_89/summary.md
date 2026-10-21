# EMA Hourly Continuation — MTL/USDT P26_89

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6162 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8396 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -3.5667 |
| sortino_ratio | -1.0977 |
| max_drawdown | 0.7289 |
| cagr | -0.3972 |
| net_avg_win | 54.8693 |
| net_avg_loss | -72.5408 |
| avg_hold_time_bars | 18.7000 |
| exposure | 0.3977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
