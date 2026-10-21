# EMA Hourly Continuation — GALA/USDT P21_200

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7897 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.1154 |
| sortino_ratio | -0.2597 |
| max_drawdown | 0.2983 |
| cagr | -0.1138 |
| net_avg_win | 76.1836 |
| net_avg_loss | -90.1783 |
| avg_hold_time_bars | 53.5468 |
| exposure | 0.6499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
