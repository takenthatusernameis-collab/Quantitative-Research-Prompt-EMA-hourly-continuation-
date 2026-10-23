# EMA Hourly Continuation — FLOW/USDT P50_55

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.2338 |
| net_win_rate | 0.3436 |
| gross_profit_factor | 0.8859 |
| gross_win_rate | 0.4227 |
| sharpe_ratio | -12.5647 |
| sortino_ratio | -5.3070 |
| max_drawdown | 0.9993 |
| cagr | -0.9441 |
| net_avg_win | 10.9700 |
| net_avg_loss | -24.5622 |
| avg_hold_time_bars | 1.8838 |
| exposure | 0.0693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
