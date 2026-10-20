# EMA Hourly Continuation — MEW/USDT P26_50

**Symbol:** MEW/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.4587 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.7487 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -6.8207 |
| sortino_ratio | -2.9323 |
| max_drawdown | 0.9732 |
| cagr | -0.7606 |
| net_avg_win | 19.4778 |
| net_avg_loss | -35.2910 |
| avg_hold_time_bars | 3.5086 |
| exposure | 0.1486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
