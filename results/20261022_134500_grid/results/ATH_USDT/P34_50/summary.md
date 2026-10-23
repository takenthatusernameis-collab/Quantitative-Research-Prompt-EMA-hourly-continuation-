# EMA Hourly Continuation — ATH/USDT P34_50

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.4163 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -7.8651 |
| sortino_ratio | -3.3478 |
| max_drawdown | 0.9816 |
| cagr | -0.8149 |
| net_avg_win | 17.9910 |
| net_avg_loss | -35.9192 |
| avg_hold_time_bars | 2.4819 |
| exposure | 0.1031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
