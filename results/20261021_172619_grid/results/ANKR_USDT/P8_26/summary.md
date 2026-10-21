# EMA Hourly Continuation — ANKR/USDT P8_26

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.6531 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9430 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -4.4773 |
| sortino_ratio | -1.8102 |
| max_drawdown | 0.8777 |
| cagr | -0.5629 |
| net_avg_win | 43.9335 |
| net_avg_loss | -59.7725 |
| avg_hold_time_bars | 6.5458 |
| exposure | 0.2371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
