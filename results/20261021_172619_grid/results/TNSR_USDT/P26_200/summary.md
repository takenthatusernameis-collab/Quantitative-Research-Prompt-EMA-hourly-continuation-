# EMA Hourly Continuation — TNSR/USDT P26_200

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7620 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -1.6596 |
| sortino_ratio | -0.4432 |
| max_drawdown | 0.4469 |
| cagr | -0.1852 |
| net_avg_win | 76.8825 |
| net_avg_loss | -91.1358 |
| avg_hold_time_bars | 34.9124 |
| exposure | 0.5593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
