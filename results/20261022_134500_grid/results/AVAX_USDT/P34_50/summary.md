# EMA Hourly Continuation — AVAX/USDT P34_50

**Symbol:** AVAX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 883 |
| net_profit_factor | 0.3658 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.8223 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -9.7768 |
| sortino_ratio | -4.1420 |
| max_drawdown | 0.9956 |
| cagr | -0.8818 |
| net_avg_win | 15.4740 |
| net_avg_loss | -30.6523 |
| avg_hold_time_bars | 2.5889 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
