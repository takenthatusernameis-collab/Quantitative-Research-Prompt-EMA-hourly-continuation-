# EMA Hourly Continuation — EDU/USDT P34_100

**Symbol:** EDU/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5350 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -4.7823 |
| sortino_ratio | -1.7826 |
| max_drawdown | 0.8863 |
| cagr | -0.5713 |
| net_avg_win | 32.2138 |
| net_avg_loss | -49.0105 |
| avg_hold_time_bars | 8.7735 |
| exposure | 0.2787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
