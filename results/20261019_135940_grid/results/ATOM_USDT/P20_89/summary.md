# EMA Hourly Continuation — ATOM/USDT P20_89

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -3.8525 |
| sortino_ratio | -1.4299 |
| max_drawdown | 0.8296 |
| cagr | -0.4914 |
| net_avg_win | 35.3655 |
| net_avg_loss | -58.5319 |
| avg_hold_time_bars | 12.3562 |
| exposure | 0.3847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
