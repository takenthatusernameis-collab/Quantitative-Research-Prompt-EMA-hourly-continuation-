# EMA Hourly Continuation — XNO/USDT P8_50

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4380 |
| gross_profit_factor | 0.8225 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -4.3142 |
| sortino_ratio | -1.6839 |
| max_drawdown | 0.8663 |
| cagr | -0.5403 |
| net_avg_win | 46.9351 |
| net_avg_loss | -56.7180 |
| avg_hold_time_bars | 10.4947 |
| exposure | 0.3616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
