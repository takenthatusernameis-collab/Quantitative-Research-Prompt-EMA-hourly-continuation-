# EMA Hourly Continuation — BCH/USDT P89_200

**Symbol:** BCH/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.7660 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0396 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -1.3066 |
| sortino_ratio | -0.3135 |
| max_drawdown | 0.3200 |
| cagr | -0.1338 |
| net_avg_win | 69.2996 |
| net_avg_loss | -95.8348 |
| avg_hold_time_bars | 14.3705 |
| exposure | 0.1816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
