# EMA Hourly Continuation — CETUS/USDT P12_21

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6945 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9681 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.6283 |
| sortino_ratio | -0.7559 |
| max_drawdown | 0.5994 |
| cagr | -0.2934 |
| net_avg_win | 68.0313 |
| net_avg_loss | -90.5329 |
| avg_hold_time_bars | 4.5690 |
| exposure | 0.0839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
