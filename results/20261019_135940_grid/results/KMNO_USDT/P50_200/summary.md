# EMA Hourly Continuation — KMNO/USDT P50_200

**Symbol:** KMNO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6659 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.9035 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -2.5862 |
| sortino_ratio | -0.7112 |
| max_drawdown | 0.5636 |
| cagr | -0.2849 |
| net_avg_win | 64.2018 |
| net_avg_loss | -85.2078 |
| avg_hold_time_bars | 21.5550 |
| exposure | 0.3712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
