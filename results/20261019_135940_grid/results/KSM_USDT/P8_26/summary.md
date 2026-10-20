# EMA Hourly Continuation — KSM/USDT P8_26

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1500 |
| net_profit_factor | 0.4429 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8818 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -9.6040 |
| sortino_ratio | -5.2319 |
| max_drawdown | 0.9985 |
| cagr | -0.9243 |
| net_avg_win | 11.8458 |
| net_avg_loss | -21.5920 |
| avg_hold_time_bars | 4.2653 |
| exposure | 0.2908 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
