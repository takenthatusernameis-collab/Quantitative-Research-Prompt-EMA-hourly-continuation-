# EMA Hourly Continuation — CVX/USDT P8_20

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1682 |
| net_profit_factor | 0.4026 |
| net_win_rate | 0.4269 |
| gross_profit_factor | 0.8394 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -11.1682 |
| sortino_ratio | -6.4313 |
| max_drawdown | 0.9997 |
| cagr | -0.9597 |
| net_avg_win | 9.3829 |
| net_avg_loss | -17.3587 |
| avg_hold_time_bars | 3.1932 |
| exposure | 0.2441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
