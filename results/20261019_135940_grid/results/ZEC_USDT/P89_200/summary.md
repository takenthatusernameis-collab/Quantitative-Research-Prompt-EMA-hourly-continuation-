# EMA Hourly Continuation — ZEC/USDT P89_200

**Symbol:** ZEC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.5122 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.7653 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -3.2550 |
| sortino_ratio | -0.8627 |
| max_drawdown | 0.6623 |
| cagr | -0.3324 |
| net_avg_win | 42.9051 |
| net_avg_loss | -65.6697 |
| avg_hold_time_bars | 12.7296 |
| exposure | 0.2054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
