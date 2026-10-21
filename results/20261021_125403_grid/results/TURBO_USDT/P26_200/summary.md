# EMA Hourly Continuation — TURBO/USDT P26_200

**Symbol:** TURBO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9836 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9629 |
| sortino_ratio | -0.2484 |
| max_drawdown | 0.2543 |
| cagr | -0.1100 |
| net_avg_win | 83.0428 |
| net_avg_loss | -98.9495 |
| avg_hold_time_bars | 37.0404 |
| exposure | 0.5496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
