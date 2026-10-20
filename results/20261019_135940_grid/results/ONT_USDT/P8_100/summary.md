# EMA Hourly Continuation — ONT/USDT P8_100

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.5911 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8640 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -4.2154 |
| sortino_ratio | -1.5704 |
| max_drawdown | 0.8524 |
| cagr | -0.5256 |
| net_avg_win | 37.9277 |
| net_avg_loss | -54.3998 |
| avg_hold_time_bars | 19.9730 |
| exposure | 0.6363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
