# EMA Hourly Continuation — KMNO/USDT P21_34

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 1.0126 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -2.0202 |
| sortino_ratio | -0.5151 |
| max_drawdown | 0.4557 |
| cagr | -0.2110 |
| net_avg_win | 64.7839 |
| net_avg_loss | -93.8068 |
| avg_hold_time_bars | 5.6431 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
