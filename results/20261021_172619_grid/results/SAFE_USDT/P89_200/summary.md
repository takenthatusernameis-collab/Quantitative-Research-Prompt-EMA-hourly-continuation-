# EMA Hourly Continuation — SAFE/USDT P89_200

**Symbol:** SAFE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7294 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.5719 |
| sortino_ratio | -0.3680 |
| max_drawdown | 0.3601 |
| cagr | -0.1555 |
| net_avg_win | 71.8684 |
| net_avg_loss | -92.1004 |
| avg_hold_time_bars | 16.1648 |
| exposure | 0.1977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
