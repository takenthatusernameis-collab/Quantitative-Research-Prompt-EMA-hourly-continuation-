# EMA Hourly Continuation — FLIP/USDT P12_200

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -1.8704 |
| sortino_ratio | -0.4056 |
| max_drawdown | 0.4151 |
| cagr | -0.1750 |
| net_avg_win | 76.0792 |
| net_avg_loss | -98.0380 |
| avg_hold_time_bars | 71.5546 |
| exposure | 0.7741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
