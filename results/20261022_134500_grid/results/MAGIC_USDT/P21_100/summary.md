# EMA Hourly Continuation — MAGIC/USDT P21_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.7387 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0347 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -2.4921 |
| sortino_ratio | -0.8567 |
| max_drawdown | 0.6519 |
| cagr | -0.3319 |
| net_avg_win | 60.6141 |
| net_avg_loss | -83.4631 |
| avg_hold_time_bars | 17.6027 |
| exposure | 0.4713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
