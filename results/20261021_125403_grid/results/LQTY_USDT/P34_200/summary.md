# EMA Hourly Continuation — LQTY/USDT P34_200

**Symbol:** LQTY/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7779 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9333 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.2880 |
| sortino_ratio | -0.3337 |
| max_drawdown | 0.3768 |
| cagr | -0.1431 |
| net_avg_win | 69.7640 |
| net_avg_loss | -85.9705 |
| avg_hold_time_bars | 32.8580 |
| exposure | 0.4921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
