# EMA Hourly Continuation — DOGE/USDT P89_100

**Symbol:** DOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.1655 |
| net_win_rate | 0.3280 |
| gross_profit_factor | 0.5717 |
| gross_win_rate | 0.3776 |
| sharpe_ratio | -11.8841 |
| sortino_ratio | -4.4836 |
| max_drawdown | 0.9979 |
| cagr | -0.9133 |
| net_avg_win | 9.6509 |
| net_avg_loss | -28.4688 |
| avg_hold_time_bars | 1.8512 |
| exposure | 0.0526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
