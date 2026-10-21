# EMA Hourly Continuation — SUI/USDT P8_20

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7806 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0375 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -1.5541 |
| sortino_ratio | -0.4560 |
| max_drawdown | 0.4519 |
| cagr | -0.1891 |
| net_avg_win | 68.3456 |
| net_avg_loss | -91.8698 |
| avg_hold_time_bars | 5.4062 |
| exposure | 0.1022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
