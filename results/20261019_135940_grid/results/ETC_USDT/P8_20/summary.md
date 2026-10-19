# EMA Hourly Continuation — ETC/USDT P8_20

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1676 |
| net_profit_factor | 0.2391 |
| net_win_rate | 0.3950 |
| gross_profit_factor | 0.7599 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -15.2013 |
| sortino_ratio | -8.9060 |
| max_drawdown | 1.0000 |
| cagr | -0.9906 |
| net_avg_win | 4.7479 |
| net_avg_loss | -12.9616 |
| avg_hold_time_bars | 2.8920 |
| exposure | 0.2203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
