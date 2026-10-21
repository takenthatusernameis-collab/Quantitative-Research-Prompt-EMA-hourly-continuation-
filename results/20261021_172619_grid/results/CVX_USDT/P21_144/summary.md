# EMA Hourly Continuation — CVX/USDT P21_144

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.2861 |
| sortino_ratio | -0.3383 |
| max_drawdown | 0.3412 |
| cagr | -0.1455 |
| net_avg_win | 74.5818 |
| net_avg_loss | -89.8994 |
| avg_hold_time_bars | 34.9029 |
| exposure | 0.5394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
