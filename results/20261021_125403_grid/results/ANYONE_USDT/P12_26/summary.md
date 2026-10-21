# EMA Hourly Continuation — ANYONE/USDT P12_26

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.7549 |
| net_win_rate | 0.4860 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -2.1196 |
| sortino_ratio | -0.6855 |
| max_drawdown | 0.5727 |
| cagr | -0.2719 |
| net_avg_win | 70.0528 |
| net_avg_loss | -87.7244 |
| avg_hold_time_bars | 5.9158 |
| exposure | 0.1384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
