# EMA Hourly Continuation — ZEC/USDT P12_55

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 972 |
| net_profit_factor | 0.5836 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.9676 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -4.9694 |
| sortino_ratio | -2.1715 |
| max_drawdown | 0.9303 |
| cagr | -0.6513 |
| net_avg_win | 27.9995 |
| net_avg_loss | -44.0045 |
| avg_hold_time_bars | 8.1502 |
| exposure | 0.3601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
