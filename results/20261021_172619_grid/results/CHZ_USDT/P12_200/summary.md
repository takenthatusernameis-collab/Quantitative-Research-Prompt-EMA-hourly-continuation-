# EMA Hourly Continuation — CHZ/USDT P12_200

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.9034 |
| net_win_rate | 0.5201 |
| gross_profit_factor | 1.0733 |
| gross_win_rate | 0.5201 |
| sharpe_ratio | -0.5243 |
| sortino_ratio | -0.1300 |
| max_drawdown | 0.3419 |
| cagr | -0.0613 |
| net_avg_win | 88.5448 |
| net_avg_loss | -106.2432 |
| avg_hold_time_bars | 54.8289 |
| exposure | 0.7427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
