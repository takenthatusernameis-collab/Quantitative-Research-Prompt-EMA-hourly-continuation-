# EMA Hourly Continuation — DEEP/USDT P21_89

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.9038 |
| net_win_rate | 0.5162 |
| gross_profit_factor | 1.0648 |
| gross_win_rate | 0.5162 |
| sharpe_ratio | -0.6597 |
| sortino_ratio | -0.1946 |
| max_drawdown | 0.3027 |
| cagr | -0.0898 |
| net_avg_win | 92.7563 |
| net_avg_loss | -109.5100 |
| avg_hold_time_bars | 19.7316 |
| exposure | 0.3787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
