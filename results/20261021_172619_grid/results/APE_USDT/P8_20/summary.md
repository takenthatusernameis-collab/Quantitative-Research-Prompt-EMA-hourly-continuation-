# EMA Hourly Continuation — APE/USDT P8_20

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -2.9036 |
| sortino_ratio | -0.9252 |
| max_drawdown | 0.6701 |
| cagr | -0.3452 |
| net_avg_win | 54.7401 |
| net_avg_loss | -74.8694 |
| avg_hold_time_bars | 5.5282 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
