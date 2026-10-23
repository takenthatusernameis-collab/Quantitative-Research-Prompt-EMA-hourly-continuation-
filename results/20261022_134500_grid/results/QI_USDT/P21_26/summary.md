# EMA Hourly Continuation — QI/USDT P21_26

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.2691 |
| net_win_rate | 0.3847 |
| gross_profit_factor | 0.7804 |
| gross_win_rate | 0.4386 |
| sharpe_ratio | -12.1435 |
| sortino_ratio | -5.6970 |
| max_drawdown | 0.9994 |
| cagr | -0.9456 |
| net_avg_win | 9.0395 |
| net_avg_loss | -21.0025 |
| avg_hold_time_bars | 2.6616 |
| exposure | 0.1274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
