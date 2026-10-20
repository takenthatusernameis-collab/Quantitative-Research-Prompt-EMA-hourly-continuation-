# EMA Hourly Continuation — VR/USDT P55_89

**Symbol:** VR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.3480 |
| net_win_rate | 0.2886 |
| gross_profit_factor | 0.6174 |
| gross_win_rate | 0.3019 |
| sharpe_ratio | -12.9674 |
| sortino_ratio | -5.1479 |
| max_drawdown | 0.9995 |
| cagr | -0.9509 |
| net_avg_win | 24.5817 |
| net_avg_loss | -28.6525 |
| avg_hold_time_bars | 3.7181 |
| exposure | 0.1271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
