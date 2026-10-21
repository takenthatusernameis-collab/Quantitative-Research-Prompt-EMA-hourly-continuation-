# EMA Hourly Continuation — JUP/USDT P34_55

**Symbol:** JUP/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.9073 |
| net_win_rate | 0.5498 |
| gross_profit_factor | 1.2101 |
| gross_win_rate | 0.5498 |
| sharpe_ratio | -0.5126 |
| sortino_ratio | -0.1354 |
| max_drawdown | 0.2770 |
| cagr | -0.0632 |
| net_avg_win | 81.2990 |
| net_avg_loss | -109.4539 |
| avg_hold_time_bars | 5.2961 |
| exposure | 0.0797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
