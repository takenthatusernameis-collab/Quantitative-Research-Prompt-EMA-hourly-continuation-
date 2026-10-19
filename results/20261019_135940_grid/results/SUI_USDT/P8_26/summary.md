# EMA Hourly Continuation — SUI/USDT P8_26

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1588 |
| net_profit_factor | 0.5139 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4616 |
| sharpe_ratio | -10.3605 |
| sortino_ratio | -5.8030 |
| max_drawdown | 0.9993 |
| cagr | -0.9456 |
| net_avg_win | 15.0072 |
| net_avg_loss | -23.2561 |
| avg_hold_time_bars | 3.5428 |
| exposure | 0.2557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
