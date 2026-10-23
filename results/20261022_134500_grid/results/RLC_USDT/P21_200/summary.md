# EMA Hourly Continuation — RLC/USDT P21_200

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6821 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9588 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.3933 |
| sortino_ratio | -0.6742 |
| max_drawdown | 0.5947 |
| cagr | -0.2767 |
| net_avg_win | 61.2513 |
| net_avg_loss | -83.7828 |
| avg_hold_time_bars | 33.2772 |
| exposure | 0.6111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
