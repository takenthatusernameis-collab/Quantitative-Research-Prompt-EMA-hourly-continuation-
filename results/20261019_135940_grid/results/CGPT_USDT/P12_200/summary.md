# EMA Hourly Continuation — CGPT/USDT P12_200

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -2.1582 |
| sortino_ratio | -0.5484 |
| max_drawdown | 0.4944 |
| cagr | -0.2300 |
| net_avg_win | 66.7149 |
| net_avg_loss | -87.2033 |
| avg_hold_time_bars | 51.8318 |
| exposure | 0.7704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
