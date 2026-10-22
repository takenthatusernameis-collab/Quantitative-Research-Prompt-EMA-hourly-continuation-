# EMA Hourly Continuation — MOVR/USDT P21_100

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.6716 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8319 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -2.9600 |
| sortino_ratio | -0.9761 |
| max_drawdown | 0.6984 |
| cagr | -0.3619 |
| net_avg_win | 56.6974 |
| net_avg_loss | -69.3530 |
| avg_hold_time_bars | 15.0739 |
| exposure | 0.3707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
