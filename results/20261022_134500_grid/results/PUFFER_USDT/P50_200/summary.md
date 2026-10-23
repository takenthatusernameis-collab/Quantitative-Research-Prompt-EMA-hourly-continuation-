# EMA Hourly Continuation — PUFFER/USDT P50_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.6049 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8288 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -2.9220 |
| sortino_ratio | -0.7772 |
| max_drawdown | 0.5534 |
| cagr | -0.3102 |
| net_avg_win | 61.6185 |
| net_avg_loss | -83.3977 |
| avg_hold_time_bars | 24.3849 |
| exposure | 0.4016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
