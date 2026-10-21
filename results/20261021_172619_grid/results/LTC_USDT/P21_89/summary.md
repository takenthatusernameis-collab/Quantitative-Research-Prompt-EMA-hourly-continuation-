# EMA Hourly Continuation — LTC/USDT P21_89

**Symbol:** LTC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.5452 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.7482 |
| gross_win_rate | 0.4320 |
| sharpe_ratio | -4.0026 |
| sortino_ratio | -1.2247 |
| max_drawdown | 0.7695 |
| cagr | -0.4318 |
| net_avg_win | 45.4471 |
| net_avg_loss | -63.3872 |
| avg_hold_time_bars | 15.7322 |
| exposure | 0.3311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
