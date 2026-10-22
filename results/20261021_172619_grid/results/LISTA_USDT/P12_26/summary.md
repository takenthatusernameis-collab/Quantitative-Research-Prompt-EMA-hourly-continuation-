# EMA Hourly Continuation — LISTA/USDT P12_26

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.6811 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -2.9770 |
| sortino_ratio | -1.0364 |
| max_drawdown | 0.6965 |
| cagr | -0.3787 |
| net_avg_win | 54.0622 |
| net_avg_loss | -73.2926 |
| avg_hold_time_bars | 5.9130 |
| exposure | 0.1596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
