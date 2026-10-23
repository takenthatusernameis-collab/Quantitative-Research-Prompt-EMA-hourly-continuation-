# EMA Hourly Continuation — RIO/USDT P89_200

**Symbol:** RIO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.5524 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.7632 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -4.0792 |
| sortino_ratio | -1.2528 |
| max_drawdown | 0.7860 |
| cagr | -0.4483 |
| net_avg_win | 46.7041 |
| net_avg_loss | -64.3613 |
| avg_hold_time_bars | 8.9216 |
| exposure | 0.1933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
