# EMA Hourly Continuation — CHZ/USDT P55_100

**Symbol:** CHZ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.5309 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -4.9110 |
| sortino_ratio | -1.7211 |
| max_drawdown | 0.8753 |
| cagr | -0.5598 |
| net_avg_win | 33.9392 |
| net_avg_loss | -58.8687 |
| avg_hold_time_bars | 5.1680 |
| exposure | 0.1426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
