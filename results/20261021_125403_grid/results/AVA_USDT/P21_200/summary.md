# EMA Hourly Continuation — AVA/USDT P21_200

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8316 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 0.9939 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -0.9262 |
| sortino_ratio | -0.2472 |
| max_drawdown | 0.3659 |
| cagr | -0.1095 |
| net_avg_win | 71.2900 |
| net_avg_loss | -87.2235 |
| avg_hold_time_bars | 35.1037 |
| exposure | 0.5537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
