# EMA Hourly Continuation — TRADE/USDT P20_26

**Symbol:** TRADE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.2636 |
| net_win_rate | 0.3250 |
| gross_profit_factor | 0.6427 |
| gross_win_rate | 0.3541 |
| sharpe_ratio | -13.3010 |
| sortino_ratio | -5.9850 |
| max_drawdown | 0.9997 |
| cagr | -0.9588 |
| net_avg_win | 11.4306 |
| net_avg_loss | -20.8838 |
| avg_hold_time_bars | 3.0685 |
| exposure | 0.1343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
