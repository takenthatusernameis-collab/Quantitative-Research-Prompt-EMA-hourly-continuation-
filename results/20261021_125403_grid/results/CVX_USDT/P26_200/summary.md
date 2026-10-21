# EMA Hourly Continuation — CVX/USDT P26_200

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7743 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9106 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -1.5093 |
| sortino_ratio | -0.4006 |
| max_drawdown | 0.3834 |
| cagr | -0.1698 |
| net_avg_win | 77.1699 |
| net_avg_loss | -90.8989 |
| avg_hold_time_bars | 32.9368 |
| exposure | 0.5210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
