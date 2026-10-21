# EMA Hourly Continuation — LINK/USDT P12_34

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.7418 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0259 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -2.4821 |
| sortino_ratio | -0.8185 |
| max_drawdown | 0.6433 |
| cagr | -0.3123 |
| net_avg_win | 66.5982 |
| net_avg_loss | -89.0964 |
| avg_hold_time_bars | 7.0985 |
| exposure | 0.1704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
