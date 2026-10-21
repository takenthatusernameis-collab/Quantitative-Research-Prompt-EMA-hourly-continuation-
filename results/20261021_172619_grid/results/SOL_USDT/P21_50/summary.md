# EMA Hourly Continuation — SOL/USDT P21_50

**Symbol:** SOL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6599 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.7717 |
| sortino_ratio | -0.8152 |
| max_drawdown | 0.6265 |
| cagr | -0.3123 |
| net_avg_win | 58.5308 |
| net_avg_loss | -81.0761 |
| avg_hold_time_bars | 7.9314 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
