# EMA Hourly Continuation — ELON/USDT P20_200

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7760 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -2.7923 |
| sortino_ratio | -0.7740 |
| max_drawdown | 0.5985 |
| cagr | -0.3000 |
| net_avg_win | 61.9488 |
| net_avg_loss | -75.5744 |
| avg_hold_time_bars | 31.8854 |
| exposure | 0.5565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
