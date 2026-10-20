# EMA Hourly Continuation — SLP/USDT P21_26

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1336 |
| net_profit_factor | 0.2449 |
| net_win_rate | 0.3496 |
| gross_profit_factor | 0.7962 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -15.6399 |
| sortino_ratio | -8.3819 |
| max_drawdown | 1.0000 |
| cagr | -0.9879 |
| net_avg_win | 6.9440 |
| net_avg_loss | -15.2390 |
| avg_hold_time_bars | 2.0516 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
