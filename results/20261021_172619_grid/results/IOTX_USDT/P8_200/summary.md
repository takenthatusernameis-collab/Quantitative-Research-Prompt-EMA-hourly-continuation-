# EMA Hourly Continuation — IOTX/USDT P8_200

**Symbol:** IOTX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.8017 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -1.0118 |
| sortino_ratio | -0.2164 |
| max_drawdown | 0.2653 |
| cagr | -0.0952 |
| net_avg_win | 80.9238 |
| net_avg_loss | -98.2884 |
| avg_hold_time_bars | 82.2444 |
| exposure | 0.8411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
