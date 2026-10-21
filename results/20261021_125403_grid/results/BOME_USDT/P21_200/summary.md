# EMA Hourly Continuation — BOME/USDT P21_200

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.8532 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9796 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.7345 |
| sortino_ratio | -0.1718 |
| max_drawdown | 0.2395 |
| cagr | -0.0780 |
| net_avg_win | 79.9685 |
| net_avg_loss | -93.7331 |
| avg_hold_time_bars | 52.2015 |
| exposure | 0.6359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
