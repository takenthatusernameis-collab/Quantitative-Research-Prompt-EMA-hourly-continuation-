# EMA Hourly Continuation — ATH/USDT P55_200

**Symbol:** ATH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.8231 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9756 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.0517 |
| sortino_ratio | -0.2621 |
| max_drawdown | 0.2712 |
| cagr | -0.1150 |
| net_avg_win | 82.5596 |
| net_avg_loss | -98.2079 |
| avg_hold_time_bars | 26.1509 |
| exposure | 0.3613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
