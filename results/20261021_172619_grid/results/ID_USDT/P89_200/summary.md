# EMA Hourly Continuation — ID/USDT P89_200

**Symbol:** ID/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.7750 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9860 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.2351 |
| sortino_ratio | -0.2877 |
| max_drawdown | 0.2862 |
| cagr | -0.1251 |
| net_avg_win | 74.1356 |
| net_avg_loss | -95.6560 |
| avg_hold_time_bars | 17.0977 |
| exposure | 0.2058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
