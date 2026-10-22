# EMA Hourly Continuation — TRADE/USDT P8_20

**Symbol:** TRADE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1422 |
| net_profit_factor | 0.4585 |
| net_win_rate | 0.3861 |
| gross_profit_factor | 0.8839 |
| gross_win_rate | 0.3994 |
| sharpe_ratio | -12.4348 |
| sortino_ratio | -6.6149 |
| max_drawdown | 0.9998 |
| cagr | -0.9673 |
| net_avg_win | 15.4172 |
| net_avg_loss | -21.1480 |
| avg_hold_time_bars | 3.8629 |
| exposure | 0.2497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
