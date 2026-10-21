# EMA Hourly Continuation — CETUS/USDT P20_26

**Symbol:** CETUS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.7316 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0535 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.7877 |
| sortino_ratio | -0.4161 |
| max_drawdown | 0.4230 |
| cagr | -0.1739 |
| net_avg_win | 78.3684 |
| net_avg_loss | -108.7613 |
| avg_hold_time_bars | 4.4583 |
| exposure | 0.0533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
