# EMA Hourly Continuation — ZK/USDT P55_200

**Symbol:** ZK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6763 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -2.3981 |
| sortino_ratio | -0.6862 |
| max_drawdown | 0.5446 |
| cagr | -0.2764 |
| net_avg_win | 60.9608 |
| net_avg_loss | -81.6232 |
| avg_hold_time_bars | 20.2846 |
| exposure | 0.3788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
