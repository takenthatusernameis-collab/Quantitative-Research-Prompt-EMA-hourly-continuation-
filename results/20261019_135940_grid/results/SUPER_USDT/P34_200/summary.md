# EMA Hourly Continuation — SUPER/USDT P34_200

**Symbol:** SUPER/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.8479 |
| net_win_rate | 0.5327 |
| gross_profit_factor | 1.1345 |
| gross_win_rate | 0.5352 |
| sharpe_ratio | -0.9849 |
| sortino_ratio | -0.2803 |
| max_drawdown | 0.3612 |
| cagr | -0.1255 |
| net_avg_win | 75.2059 |
| net_avg_loss | -101.0913 |
| avg_hold_time_bars | 27.1382 |
| exposure | 0.4910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
