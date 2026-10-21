# EMA Hourly Continuation — POPCAT/USDT P21_89

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.7292 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8697 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -2.1703 |
| sortino_ratio | -0.6722 |
| max_drawdown | 0.4906 |
| cagr | -0.2666 |
| net_avg_win | 68.8251 |
| net_avg_loss | -82.6969 |
| avg_hold_time_bars | 16.7995 |
| exposure | 0.3630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
