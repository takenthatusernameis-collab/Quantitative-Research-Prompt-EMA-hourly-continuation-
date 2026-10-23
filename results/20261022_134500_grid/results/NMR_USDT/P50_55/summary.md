# EMA Hourly Continuation — NMR/USDT P50_55

**Symbol:** NMR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.1981 |
| net_win_rate | 0.3562 |
| gross_profit_factor | 0.6984 |
| gross_win_rate | 0.4354 |
| sharpe_ratio | -12.6262 |
| sortino_ratio | -5.4102 |
| max_drawdown | 0.9994 |
| cagr | -0.9483 |
| net_avg_win | 8.0676 |
| net_avg_loss | -22.5368 |
| avg_hold_time_bars | 2.0978 |
| exposure | 0.0819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
