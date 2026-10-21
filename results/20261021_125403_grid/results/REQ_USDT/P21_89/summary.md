# EMA Hourly Continuation — REQ/USDT P21_89

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 548 |
| net_profit_factor | 0.6959 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9952 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -3.2050 |
| sortino_ratio | -1.0728 |
| max_drawdown | 0.7241 |
| cagr | -0.3902 |
| net_avg_win | 61.1764 |
| net_avg_loss | -82.9262 |
| avg_hold_time_bars | 14.5584 |
| exposure | 0.3626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
