# EMA Hourly Continuation — ENA/USDT P20_26

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1224 |
| net_profit_factor | 0.3450 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7408 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -10.6418 |
| sortino_ratio | -5.2733 |
| max_drawdown | 0.9989 |
| cagr | -0.9323 |
| net_avg_win | 10.1002 |
| net_avg_loss | -21.6937 |
| avg_hold_time_bars | 1.8758 |
| exposure | 0.1044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
