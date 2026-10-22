# EMA Hourly Continuation — SHIB/USDT P8_26

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1573 |
| net_profit_factor | 0.3718 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8159 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -11.6829 |
| sortino_ratio | -6.5168 |
| max_drawdown | 0.9998 |
| cagr | -0.9650 |
| net_avg_win | 8.5634 |
| net_avg_loss | -18.0444 |
| avg_hold_time_bars | 3.6122 |
| exposure | 0.2583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
