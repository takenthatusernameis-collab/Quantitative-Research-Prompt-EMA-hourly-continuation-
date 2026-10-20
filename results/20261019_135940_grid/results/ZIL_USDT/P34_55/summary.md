# EMA Hourly Continuation — ZIL/USDT P34_55

**Symbol:** ZIL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.3371 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.7801 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -9.3496 |
| sortino_ratio | -4.0370 |
| max_drawdown | 0.9939 |
| cagr | -0.8673 |
| net_avg_win | 12.9880 |
| net_avg_loss | -28.6063 |
| avg_hold_time_bars | 3.0898 |
| exposure | 0.1282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
