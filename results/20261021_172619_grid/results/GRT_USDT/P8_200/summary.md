# EMA Hourly Continuation — GRT/USDT P8_200

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.9520 |
| net_win_rate | 0.5236 |
| gross_profit_factor | 1.0749 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -0.1635 |
| sortino_ratio | -0.0324 |
| max_drawdown | 0.1867 |
| cagr | -0.0179 |
| net_avg_win | 88.1283 |
| net_avg_loss | -101.7281 |
| avg_hold_time_bars | 98.3717 |
| exposure | 0.8502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
