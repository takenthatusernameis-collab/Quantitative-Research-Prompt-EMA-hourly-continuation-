# EMA Hourly Continuation — CELO/USDT P12_21

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5976 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8813 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -3.6107 |
| sortino_ratio | -1.0896 |
| max_drawdown | 0.7238 |
| cagr | -0.3939 |
| net_avg_win | 51.7140 |
| net_avg_loss | -74.2710 |
| avg_hold_time_bars | 4.9596 |
| exposure | 0.1001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
