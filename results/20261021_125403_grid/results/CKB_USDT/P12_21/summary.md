# EMA Hourly Continuation — CKB/USDT P12_21

**Symbol:** CKB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8892 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.1838 |
| sortino_ratio | -0.9130 |
| max_drawdown | 0.6634 |
| cagr | -0.3422 |
| net_avg_win | 56.3709 |
| net_avg_loss | -80.3018 |
| avg_hold_time_bars | 4.4539 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
