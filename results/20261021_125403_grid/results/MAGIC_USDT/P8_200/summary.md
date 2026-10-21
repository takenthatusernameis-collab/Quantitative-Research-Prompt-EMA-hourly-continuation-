# EMA Hourly Continuation — MAGIC/USDT P8_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.8545 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -0.9418 |
| sortino_ratio | -0.2343 |
| max_drawdown | 0.4377 |
| cagr | -0.1041 |
| net_avg_win | 93.2359 |
| net_avg_loss | -110.5670 |
| avg_hold_time_bars | 57.9338 |
| exposure | 0.7953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
