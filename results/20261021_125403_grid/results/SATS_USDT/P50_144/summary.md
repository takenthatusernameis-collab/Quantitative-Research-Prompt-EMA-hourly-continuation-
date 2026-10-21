# EMA Hourly Continuation — SATS/USDT P50_144

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.6887 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.8722 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -2.1992 |
| sortino_ratio | -0.5687 |
| max_drawdown | 0.5219 |
| cagr | -0.2301 |
| net_avg_win | 70.2854 |
| net_avg_loss | -85.7030 |
| avg_hold_time_bars | 17.1712 |
| exposure | 0.2587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
