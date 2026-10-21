# EMA Hourly Continuation — IO/USDT P26_50

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8082 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.3289 |
| sortino_ratio | -0.3638 |
| max_drawdown | 0.3605 |
| cagr | -0.1546 |
| net_avg_win | 80.0900 |
| net_avg_loss | -100.2654 |
| avg_hold_time_bars | 6.1696 |
| exposure | 0.1021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
