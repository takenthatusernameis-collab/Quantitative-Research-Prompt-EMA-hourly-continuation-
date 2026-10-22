# EMA Hourly Continuation — AGLD/USDT P20_200

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7492 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8930 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -1.9346 |
| sortino_ratio | -0.5300 |
| max_drawdown | 0.5366 |
| cagr | -0.2169 |
| net_avg_win | 79.0118 |
| net_avg_loss | -91.7558 |
| avg_hold_time_bars | 35.7567 |
| exposure | 0.6052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
