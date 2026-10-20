# EMA Hourly Continuation — NMR/USDT P21_34

**Symbol:** NMR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.4426 |
| net_win_rate | 0.4089 |
| gross_profit_factor | 0.9352 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -11.2046 |
| sortino_ratio | -5.4943 |
| max_drawdown | 0.9992 |
| cagr | -0.9398 |
| net_avg_win | 16.2256 |
| net_avg_loss | -25.3546 |
| avg_hold_time_bars | 2.9749 |
| exposure | 0.1617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
