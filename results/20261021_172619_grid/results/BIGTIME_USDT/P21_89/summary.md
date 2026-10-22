# EMA Hourly Continuation — BIGTIME/USDT P21_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8398 |
| net_win_rate | 0.5131 |
| gross_profit_factor | 1.0474 |
| gross_win_rate | 0.5131 |
| sharpe_ratio | -1.2099 |
| sortino_ratio | -0.3857 |
| max_drawdown | 0.4228 |
| cagr | -0.1645 |
| net_avg_win | 75.2219 |
| net_avg_loss | -94.4032 |
| avg_hold_time_bars | 18.1152 |
| exposure | 0.4058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
