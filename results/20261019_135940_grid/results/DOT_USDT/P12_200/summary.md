# EMA Hourly Continuation — DOT/USDT P12_200

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.5602 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -2.8587 |
| sortino_ratio | -0.6479 |
| max_drawdown | 0.5665 |
| cagr | -0.2765 |
| net_avg_win | 57.6144 |
| net_avg_loss | -87.8525 |
| avg_hold_time_bars | 66.7228 |
| exposure | 0.8098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
