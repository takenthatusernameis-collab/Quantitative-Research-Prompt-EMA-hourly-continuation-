# EMA Hourly Continuation — GLM/USDT P8_89

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -4.6940 |
| sortino_ratio | -1.8030 |
| max_drawdown | 0.8895 |
| cagr | -0.5745 |
| net_avg_win | 35.2489 |
| net_avg_loss | -50.9594 |
| avg_hold_time_bars | 18.5635 |
| exposure | 0.6244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
