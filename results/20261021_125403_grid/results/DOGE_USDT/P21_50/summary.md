# EMA Hourly Continuation — DOGE/USDT P21_50

**Symbol:** DOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6802 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.6476 |
| sortino_ratio | -0.7994 |
| max_drawdown | 0.6232 |
| cagr | -0.3065 |
| net_avg_win | 59.4831 |
| net_avg_loss | -81.7431 |
| avg_hold_time_bars | 8.0404 |
| exposure | 0.1626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
