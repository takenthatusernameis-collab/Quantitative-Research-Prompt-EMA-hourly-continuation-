# EMA Hourly Continuation — ENA/USDT P12_100

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.7769 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.9501 |
| sortino_ratio | -0.6893 |
| max_drawdown | 0.5863 |
| cagr | -0.2836 |
| net_avg_win | 60.9745 |
| net_avg_loss | -81.4987 |
| avg_hold_time_bars | 19.5220 |
| exposure | 0.5644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
