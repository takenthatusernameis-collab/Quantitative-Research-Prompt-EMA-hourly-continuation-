# EMA Hourly Continuation — XAI/USDT P20_55

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.7478 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9507 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.6284 |
| sortino_ratio | -0.9316 |
| max_drawdown | 0.6871 |
| cagr | -0.3482 |
| net_avg_win | 65.7419 |
| net_avg_loss | -81.5978 |
| avg_hold_time_bars | 8.3047 |
| exposure | 0.2329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
