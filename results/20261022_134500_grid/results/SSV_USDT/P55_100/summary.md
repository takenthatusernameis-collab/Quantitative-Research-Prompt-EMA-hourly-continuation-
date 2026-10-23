# EMA Hourly Continuation — SSV/USDT P55_100

**Symbol:** SSV/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.4910 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -5.8802 |
| sortino_ratio | -2.1977 |
| max_drawdown | 0.9393 |
| cagr | -0.6600 |
| net_avg_win | 28.1634 |
| net_avg_loss | -46.5855 |
| avg_hold_time_bars | 5.0168 |
| exposure | 0.1621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
