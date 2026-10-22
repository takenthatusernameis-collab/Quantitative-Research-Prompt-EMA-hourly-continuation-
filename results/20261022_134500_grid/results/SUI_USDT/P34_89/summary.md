# EMA Hourly Continuation — SUI/USDT P34_89

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.5919 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9582 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -4.8177 |
| sortino_ratio | -1.7928 |
| max_drawdown | 0.8973 |
| cagr | -0.5867 |
| net_avg_win | 38.2403 |
| net_avg_loss | -59.5038 |
| avg_hold_time_bars | 6.9191 |
| exposure | 0.2217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
