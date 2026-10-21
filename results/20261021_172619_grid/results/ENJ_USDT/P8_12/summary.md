# EMA Hourly Continuation — ENJ/USDT P8_12

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.8431 |
| net_win_rate | 0.5517 |
| gross_profit_factor | 1.2149 |
| gross_win_rate | 0.5517 |
| sharpe_ratio | -0.8053 |
| sortino_ratio | -0.1885 |
| max_drawdown | 0.2615 |
| cagr | -0.0835 |
| net_avg_win | 73.6576 |
| net_avg_loss | -107.5273 |
| avg_hold_time_bars | 4.8621 |
| exposure | 0.0574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
