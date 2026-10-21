# EMA Hourly Continuation — NEO/USDT P21_200

**Symbol:** NEO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7258 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.8944 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -1.5728 |
| sortino_ratio | -0.3741 |
| max_drawdown | 0.3922 |
| cagr | -0.1589 |
| net_avg_win | 70.1233 |
| net_avg_loss | -88.0178 |
| avg_hold_time_bars | 52.2867 |
| exposure | 0.6631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
