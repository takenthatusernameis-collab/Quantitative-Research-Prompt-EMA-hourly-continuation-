# EMA Hourly Continuation — NEAR/USDT P34_50

**Symbol:** NEAR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 912 |
| net_profit_factor | 0.4061 |
| net_win_rate | 0.4452 |
| gross_profit_factor | 0.8273 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -8.1974 |
| sortino_ratio | -3.5040 |
| max_drawdown | 0.9878 |
| cagr | -0.8264 |
| net_avg_win | 16.6347 |
| net_avg_loss | -32.8668 |
| avg_hold_time_bars | 2.5033 |
| exposure | 0.1038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
