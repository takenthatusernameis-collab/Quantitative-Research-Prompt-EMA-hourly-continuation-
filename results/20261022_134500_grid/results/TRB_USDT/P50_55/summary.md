# EMA Hourly Continuation — TRB/USDT P50_55

**Symbol:** TRB/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.1958 |
| net_win_rate | 0.3245 |
| gross_profit_factor | 0.6046 |
| gross_win_rate | 0.3905 |
| sharpe_ratio | -14.1426 |
| sortino_ratio | -6.3500 |
| max_drawdown | 0.9998 |
| cagr | -0.9677 |
| net_avg_win | 8.2536 |
| net_avg_loss | -20.2493 |
| avg_hold_time_bars | 1.8713 |
| exposure | 0.0770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
