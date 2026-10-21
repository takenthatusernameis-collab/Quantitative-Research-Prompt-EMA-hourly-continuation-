# EMA Hourly Continuation — WIN/USDT P34_55

**Symbol:** WIN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.5748 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.8181 |
| sortino_ratio | -0.6616 |
| max_drawdown | 0.5590 |
| cagr | -0.2613 |
| net_avg_win | 57.1383 |
| net_avg_loss | -89.4654 |
| avg_hold_time_bars | 5.9098 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
