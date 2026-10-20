# EMA Hourly Continuation — CARV/USDT P100_200

**Symbol:** CARV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.5221 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8094 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -3.4109 |
| sortino_ratio | -0.9107 |
| max_drawdown | 0.6019 |
| cagr | -0.3548 |
| net_avg_win | 48.0083 |
| net_avg_loss | -77.0095 |
| avg_hold_time_bars | 11.5000 |
| exposure | 0.1903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
