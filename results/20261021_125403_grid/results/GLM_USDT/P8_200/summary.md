# EMA Hourly Continuation — GLM/USDT P8_200

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7017 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8834 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.2617 |
| sortino_ratio | -0.6156 |
| max_drawdown | 0.5441 |
| cagr | -0.2475 |
| net_avg_win | 69.7966 |
| net_avg_loss | -87.2910 |
| avg_hold_time_bars | 45.0815 |
| exposure | 0.7541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
