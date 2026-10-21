# EMA Hourly Continuation — ROSE/USDT P12_100

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.7247 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 1.0110 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -2.6591 |
| sortino_ratio | -0.9018 |
| max_drawdown | 0.6820 |
| cagr | -0.3462 |
| net_avg_win | 61.0098 |
| net_avg_loss | -81.8775 |
| avg_hold_time_bars | 24.2509 |
| exposure | 0.6327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
