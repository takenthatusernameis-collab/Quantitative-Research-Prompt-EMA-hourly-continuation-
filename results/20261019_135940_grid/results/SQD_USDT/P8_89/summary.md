# EMA Hourly Continuation — SQD/USDT P8_89

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 788 |
| net_profit_factor | 0.6775 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -3.4022 |
| sortino_ratio | -1.3686 |
| max_drawdown | 0.8030 |
| cagr | -0.4767 |
| net_avg_win | 44.1545 |
| net_avg_loss | -59.7835 |
| avg_hold_time_bars | 14.7970 |
| exposure | 0.5481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
