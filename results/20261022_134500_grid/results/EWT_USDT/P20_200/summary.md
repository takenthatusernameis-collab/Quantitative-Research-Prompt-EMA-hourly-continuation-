# EMA Hourly Continuation — EWT/USDT P20_200

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.5751 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.7987 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -4.0830 |
| sortino_ratio | -1.2950 |
| max_drawdown | 0.8231 |
| cagr | -0.4638 |
| net_avg_win | 48.0107 |
| net_avg_loss | -63.9729 |
| avg_hold_time_bars | 22.0409 |
| exposure | 0.5150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
