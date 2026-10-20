# EMA Hourly Continuation — RLC/USDT P21_34

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.3987 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -9.2490 |
| sortino_ratio | -4.2486 |
| max_drawdown | 0.9954 |
| cagr | -0.8806 |
| net_avg_win | 14.2521 |
| net_avg_loss | -28.2434 |
| avg_hold_time_bars | 3.0810 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
