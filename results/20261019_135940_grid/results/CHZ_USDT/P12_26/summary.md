# EMA Hourly Continuation — CHZ/USDT P12_26

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1460 |
| net_profit_factor | 0.4127 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -11.3159 |
| sortino_ratio | -6.1308 |
| max_drawdown | 0.9996 |
| cagr | -0.9540 |
| net_avg_win | 11.2945 |
| net_avg_loss | -20.3112 |
| avg_hold_time_bars | 2.8185 |
| exposure | 0.1870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
