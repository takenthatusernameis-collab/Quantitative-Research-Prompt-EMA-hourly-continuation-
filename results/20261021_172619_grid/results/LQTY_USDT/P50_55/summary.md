# EMA Hourly Continuation — LQTY/USDT P50_55

**Symbol:** LQTY/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.5867 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.1103 |
| sortino_ratio | -0.3973 |
| max_drawdown | 0.3856 |
| cagr | -0.1643 |
| net_avg_win | 63.8238 |
| net_avg_loss | -95.7827 |
| avg_hold_time_bars | 5.2081 |
| exposure | 0.0408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
