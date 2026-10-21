# EMA Hourly Continuation — XEC/USDT P8_100

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.7869 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0185 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.7513 |
| sortino_ratio | -0.5748 |
| max_drawdown | 0.5425 |
| cagr | -0.2334 |
| net_avg_win | 67.5912 |
| net_avg_loss | -87.8661 |
| avg_hold_time_bars | 27.6307 |
| exposure | 0.6602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
