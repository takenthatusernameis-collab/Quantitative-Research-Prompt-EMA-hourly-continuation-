# EMA Hourly Continuation — NMR/USDT P21_89

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7337 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.3473 |
| sortino_ratio | -0.7734 |
| max_drawdown | 0.6086 |
| cagr | -0.2990 |
| net_avg_win | 62.5389 |
| net_avg_loss | -81.1781 |
| avg_hold_time_bars | 15.4728 |
| exposure | 0.3749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
