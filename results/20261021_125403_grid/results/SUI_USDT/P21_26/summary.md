# EMA Hourly Continuation — SUI/USDT P21_26

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.7082 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9756 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.3253 |
| sortino_ratio | -0.2314 |
| max_drawdown | 0.2689 |
| cagr | -0.0999 |
| net_avg_win | 77.2335 |
| net_avg_loss | -106.1462 |
| avg_hold_time_bars | 4.5878 |
| exposure | 0.0309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
