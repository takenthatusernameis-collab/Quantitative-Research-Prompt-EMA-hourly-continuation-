# EMA Hourly Continuation — XAI/USDT P8_26

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1632 |
| net_profit_factor | 0.5667 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -10.0515 |
| sortino_ratio | -5.7107 |
| max_drawdown | 0.9991 |
| cagr | -0.9396 |
| net_avg_win | 18.5079 |
| net_avg_loss | -24.9005 |
| avg_hold_time_bars | 3.8425 |
| exposure | 0.2850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
