# EMA Hourly Continuation — FLOKI/USDT P34_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6695 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -2.4494 |
| sortino_ratio | -0.6445 |
| max_drawdown | 0.5441 |
| cagr | -0.2642 |
| net_avg_win | 65.1789 |
| net_avg_loss | -88.8392 |
| avg_hold_time_bars | 34.1714 |
| exposure | 0.5436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
