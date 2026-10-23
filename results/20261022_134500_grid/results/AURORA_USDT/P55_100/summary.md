# EMA Hourly Continuation — AURORA/USDT P55_100

**Symbol:** AURORA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 543 |
| net_profit_factor | 0.4327 |
| net_win_rate | 0.4254 |
| gross_profit_factor | 0.8333 |
| gross_win_rate | 0.4383 |
| sharpe_ratio | -6.4892 |
| sortino_ratio | -2.1126 |
| max_drawdown | 0.9370 |
| cagr | -0.6641 |
| net_avg_win | 30.8880 |
| net_avg_loss | -52.8496 |
| avg_hold_time_bars | 6.3775 |
| exposure | 0.1574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
