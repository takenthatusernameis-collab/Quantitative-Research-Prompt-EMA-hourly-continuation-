# EMA Hourly Continuation — SWFTC/USDT P20_34

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.5819 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -2.7648 |
| sortino_ratio | -0.6576 |
| max_drawdown | 0.5469 |
| cagr | -0.2605 |
| net_avg_win | 59.1716 |
| net_avg_loss | -83.0712 |
| avg_hold_time_bars | 6.7770 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
