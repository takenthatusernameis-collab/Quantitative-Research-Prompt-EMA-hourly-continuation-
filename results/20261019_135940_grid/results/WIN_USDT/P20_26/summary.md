# EMA Hourly Continuation — WIN/USDT P20_26

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1162 |
| net_profit_factor | 0.1227 |
| net_win_rate | 0.3029 |
| gross_profit_factor | 0.5523 |
| gross_win_rate | 0.3632 |
| sharpe_ratio | -17.6236 |
| sortino_ratio | -9.2170 |
| max_drawdown | 1.0000 |
| cagr | -0.9939 |
| net_avg_win | 3.9749 |
| net_avg_loss | -14.0730 |
| avg_hold_time_bars | 1.9897 |
| exposure | 0.1051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
