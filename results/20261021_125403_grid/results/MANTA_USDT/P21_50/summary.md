# EMA Hourly Continuation — MANTA/USDT P21_50

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6859 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -2.8227 |
| sortino_ratio | -0.8906 |
| max_drawdown | 0.6519 |
| cagr | -0.3353 |
| net_avg_win | 61.1716 |
| net_avg_loss | -78.2505 |
| avg_hold_time_bars | 8.7551 |
| exposure | 0.1950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
