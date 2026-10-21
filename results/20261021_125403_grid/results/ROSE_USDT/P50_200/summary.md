# EMA Hourly Continuation — ROSE/USDT P50_200

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.9919 |
| net_win_rate | 0.5441 |
| gross_profit_factor | 1.1832 |
| gross_win_rate | 0.5441 |
| sharpe_ratio | 0.0115 |
| sortino_ratio | 0.0027 |
| max_drawdown | 0.1213 |
| cagr | -0.0042 |
| net_avg_win | 87.7474 |
| net_avg_loss | -105.5824 |
| avg_hold_time_bars | 35.0588 |
| exposure | 0.4335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
