# EMA Hourly Continuation — ATOM/USDT P144_200

**Symbol:** ATOM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.6280 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8944 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -1.9082 |
| sortino_ratio | -0.3647 |
| max_drawdown | 0.3462 |
| cagr | -0.1534 |
| net_avg_win | 68.6787 |
| net_avg_loss | -97.7281 |
| avg_hold_time_bars | 6.7978 |
| exposure | 0.0550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
