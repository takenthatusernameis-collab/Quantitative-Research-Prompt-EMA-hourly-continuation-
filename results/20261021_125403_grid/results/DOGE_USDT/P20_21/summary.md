# EMA Hourly Continuation — DOGE/USDT P20_21

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 111 |
| net_profit_factor | 0.5581 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.7845 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -1.8895 |
| sortino_ratio | -0.2841 |
| max_drawdown | 0.2807 |
| cagr | -0.1230 |
| net_avg_win | 72.3435 |
| net_avg_loss | -102.4497 |
| avg_hold_time_bars | 4.4144 |
| exposure | 0.0223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
