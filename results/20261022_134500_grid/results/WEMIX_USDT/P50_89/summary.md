# EMA Hourly Continuation — WEMIX/USDT P50_89

**Symbol:** WEMIX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.2053 |
| net_win_rate | 0.2697 |
| gross_profit_factor | 0.4149 |
| gross_win_rate | 0.2882 |
| sharpe_ratio | -15.6632 |
| sortino_ratio | -7.5209 |
| max_drawdown | 0.9999 |
| cagr | -0.9801 |
| net_avg_win | 8.8756 |
| net_avg_loss | -15.9674 |
| avg_hold_time_bars | 4.0918 |
| exposure | 0.2007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
