# EMA Hourly Continuation — FIL/USDT P21_89

**Symbol:** FIL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.5079 |
| net_win_rate | 0.4362 |
| gross_profit_factor | 0.8105 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -5.7511 |
| sortino_ratio | -2.1688 |
| max_drawdown | 0.9301 |
| cagr | -0.6455 |
| net_avg_win | 30.7356 |
| net_avg_loss | -46.8138 |
| avg_hold_time_bars | 11.1136 |
| exposure | 0.3602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
