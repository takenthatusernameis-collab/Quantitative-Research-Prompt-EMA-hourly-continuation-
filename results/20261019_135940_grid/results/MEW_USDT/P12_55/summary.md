# EMA Hourly Continuation — MEW/USDT P12_55

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.5977 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8736 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -5.2383 |
| sortino_ratio | -2.2825 |
| max_drawdown | 0.9371 |
| cagr | -0.6662 |
| net_avg_win | 30.8469 |
| net_avg_loss | -45.2845 |
| avg_hold_time_bars | 9.0767 |
| exposure | 0.3981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
