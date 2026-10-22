# EMA Hourly Continuation — AGLD/USDT P12_200

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7912 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -1.5422 |
| sortino_ratio | -0.4133 |
| max_drawdown | 0.4657 |
| cagr | -0.1739 |
| net_avg_win | 85.2372 |
| net_avg_loss | -98.4645 |
| avg_hold_time_bars | 43.8455 |
| exposure | 0.7064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
