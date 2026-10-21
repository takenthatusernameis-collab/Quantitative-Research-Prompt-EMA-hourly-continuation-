# EMA Hourly Continuation — CHR/USDT P21_26

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6609 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9376 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.1191 |
| sortino_ratio | -0.4950 |
| max_drawdown | 0.4449 |
| cagr | -0.2025 |
| net_avg_win | 65.7272 |
| net_avg_loss | -92.9625 |
| avg_hold_time_bars | 5.9888 |
| exposure | 0.0724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
