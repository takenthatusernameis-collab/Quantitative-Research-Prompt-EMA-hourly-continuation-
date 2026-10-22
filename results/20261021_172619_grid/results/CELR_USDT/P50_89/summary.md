# EMA Hourly Continuation — CELR/USDT P50_89

**Symbol:** CELR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7013 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9516 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.4231 |
| sortino_ratio | -0.7328 |
| max_drawdown | 0.5898 |
| cagr | -0.2851 |
| net_avg_win | 61.5105 |
| net_avg_loss | -83.1321 |
| avg_hold_time_bars | 7.1138 |
| exposure | 0.1442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
