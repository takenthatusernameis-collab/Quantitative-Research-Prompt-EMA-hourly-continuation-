# EMA Hourly Continuation — EIGEN/USDT P50_200

**Symbol:** EIGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7050 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9359 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.4753 |
| sortino_ratio | -0.7235 |
| max_drawdown | 0.5279 |
| cagr | -0.2922 |
| net_avg_win | 71.8322 |
| net_avg_loss | -93.5776 |
| avg_hold_time_bars | 19.7677 |
| exposure | 0.3883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
