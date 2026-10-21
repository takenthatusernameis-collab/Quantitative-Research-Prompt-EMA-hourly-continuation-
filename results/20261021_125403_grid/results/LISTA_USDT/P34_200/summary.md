# EMA Hourly Continuation — LISTA/USDT P34_200

**Symbol:** LISTA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7829 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9335 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.3191 |
| sortino_ratio | -0.3412 |
| max_drawdown | 0.3096 |
| cagr | -0.1467 |
| net_avg_win | 74.9039 |
| net_avg_loss | -90.8039 |
| avg_hold_time_bars | 32.0000 |
| exposure | 0.4788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
