# EMA Hourly Continuation — CAKE/USDT P89_200

**Symbol:** CAKE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7290 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 0.9834 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -1.4693 |
| sortino_ratio | -0.3290 |
| max_drawdown | 0.3529 |
| cagr | -0.1405 |
| net_avg_win | 69.1802 |
| net_avg_loss | -95.6767 |
| avg_hold_time_bars | 13.6204 |
| exposure | 0.1517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
