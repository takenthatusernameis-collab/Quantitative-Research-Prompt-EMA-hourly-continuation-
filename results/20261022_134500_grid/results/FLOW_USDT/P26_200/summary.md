# EMA Hourly Continuation — FLOW/USDT P26_200

**Symbol:** FLOW/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.5785 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8244 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -3.4192 |
| sortino_ratio | -0.9314 |
| max_drawdown | 0.6947 |
| cagr | -0.3664 |
| net_avg_win | 54.7444 |
| net_avg_loss | -75.6196 |
| avg_hold_time_bars | 33.0779 |
| exposure | 0.5789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
