# EMA Hourly Continuation — CETUS/USDT P34_200

**Symbol:** CETUS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.9548 |
| net_win_rate | 0.5320 |
| gross_profit_factor | 1.1350 |
| gross_win_rate | 0.5320 |
| sharpe_ratio | -0.1929 |
| sortino_ratio | -0.0439 |
| max_drawdown | 0.1699 |
| cagr | -0.0240 |
| net_avg_win | 94.3059 |
| net_avg_loss | -112.2826 |
| avg_hold_time_bars | 50.8760 |
| exposure | 0.5756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
