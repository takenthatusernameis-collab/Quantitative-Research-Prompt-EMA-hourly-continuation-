# EMA Hourly Continuation — ETC/USDT P12_55

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1079 |
| net_profit_factor | 0.4725 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -7.8660 |
| sortino_ratio | -3.6267 |
| max_drawdown | 0.9890 |
| cagr | -0.8338 |
| net_avg_win | 17.8972 |
| net_avg_loss | -32.1040 |
| avg_hold_time_bars | 6.9398 |
| exposure | 0.3404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
