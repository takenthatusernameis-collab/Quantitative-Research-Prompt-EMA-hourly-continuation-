# EMA Hourly Continuation — ENJ/USDT P20_200

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9290 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.1102 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.3583 |
| sortino_ratio | -0.0871 |
| max_drawdown | 0.2598 |
| cagr | -0.0431 |
| net_avg_win | 91.2097 |
| net_avg_loss | -109.0079 |
| avg_hold_time_bars | 49.6098 |
| exposure | 0.6443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
