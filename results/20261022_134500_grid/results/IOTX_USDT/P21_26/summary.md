# EMA Hourly Continuation — IOTX/USDT P21_26

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1174 |
| net_profit_factor | 0.2322 |
| net_win_rate | 0.3492 |
| gross_profit_factor | 0.7259 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -15.0500 |
| sortino_ratio | -7.5992 |
| max_drawdown | 1.0000 |
| cagr | -0.9824 |
| net_avg_win | 7.3772 |
| net_avg_loss | -17.0474 |
| avg_hold_time_bars | 1.9753 |
| exposure | 0.1054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
