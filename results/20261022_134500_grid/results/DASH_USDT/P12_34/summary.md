# EMA Hourly Continuation — DASH/USDT P12_34

**Symbol:** DASH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1282 |
| net_profit_factor | 0.2696 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7702 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -9.6831 |
| sortino_ratio | -4.8684 |
| max_drawdown | 0.9979 |
| cagr | -0.9145 |
| net_avg_win | 6.5777 |
| net_avg_loss | -18.9234 |
| avg_hold_time_bars | 4.1256 |
| exposure | 0.2404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
