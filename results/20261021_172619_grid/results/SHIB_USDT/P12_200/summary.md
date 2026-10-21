# EMA Hourly Continuation — SHIB/USDT P12_200

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.8127 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -1.0546 |
| sortino_ratio | -0.2397 |
| max_drawdown | 0.3013 |
| cagr | -0.1053 |
| net_avg_win | 84.6148 |
| net_avg_loss | -101.6806 |
| avg_hold_time_bars | 65.2332 |
| exposure | 0.7502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
