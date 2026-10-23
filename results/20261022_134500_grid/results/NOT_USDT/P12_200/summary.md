# EMA Hourly Continuation — NOT/USDT P12_200

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 220 |
| net_profit_factor | 0.6246 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.9053 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -2.3147 |
| sortino_ratio | -0.4883 |
| max_drawdown | 0.4610 |
| cagr | -0.2103 |
| net_avg_win | 71.1970 |
| net_avg_loss | -98.5352 |
| avg_hold_time_bars | 82.7818 |
| exposure | 0.8555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
