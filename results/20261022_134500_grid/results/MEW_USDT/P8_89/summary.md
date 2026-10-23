# EMA Hourly Continuation — MEW/USDT P8_89

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.6092 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8501 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -4.1709 |
| sortino_ratio | -1.5655 |
| max_drawdown | 0.8561 |
| cagr | -0.5267 |
| net_avg_win | 40.1342 |
| net_avg_loss | -56.1558 |
| avg_hold_time_bars | 19.1734 |
| exposure | 0.6231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
