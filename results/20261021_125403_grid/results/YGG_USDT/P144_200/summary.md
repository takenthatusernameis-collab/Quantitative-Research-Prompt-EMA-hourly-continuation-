# EMA Hourly Continuation — YGG/USDT P144_200

**Symbol:** YGG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4975 |
| sharpe_ratio | -1.3748 |
| sortino_ratio | -0.2781 |
| max_drawdown | 0.2910 |
| cagr | -0.1203 |
| net_avg_win | 74.5315 |
| net_avg_loss | -101.1492 |
| avg_hold_time_bars | 9.0348 |
| exposure | 0.0822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
