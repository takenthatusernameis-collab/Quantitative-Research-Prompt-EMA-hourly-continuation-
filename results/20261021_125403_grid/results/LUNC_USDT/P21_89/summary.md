# EMA Hourly Continuation — LUNC/USDT P21_89

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6188 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8135 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -3.1038 |
| sortino_ratio | -0.9908 |
| max_drawdown | 0.6948 |
| cagr | -0.3656 |
| net_avg_win | 47.8638 |
| net_avg_loss | -65.6904 |
| avg_hold_time_bars | 13.7097 |
| exposure | 0.3135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
