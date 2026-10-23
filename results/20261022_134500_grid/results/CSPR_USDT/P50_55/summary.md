# EMA Hourly Continuation — CSPR/USDT P50_55

**Symbol:** CSPR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1078 |
| net_profit_factor | 0.1396 |
| net_win_rate | 0.2922 |
| gross_profit_factor | 0.5845 |
| gross_win_rate | 0.3386 |
| sharpe_ratio | -15.8801 |
| sortino_ratio | -7.7226 |
| max_drawdown | 1.0000 |
| cagr | -0.9862 |
| net_avg_win | 5.1505 |
| net_avg_loss | -15.2322 |
| avg_hold_time_bars | 1.9072 |
| exposure | 0.0935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
