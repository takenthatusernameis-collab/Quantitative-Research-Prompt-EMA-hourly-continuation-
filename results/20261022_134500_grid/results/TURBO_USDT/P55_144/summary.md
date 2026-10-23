# EMA Hourly Continuation — TURBO/USDT P55_144

**Symbol:** TURBO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7362 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0677 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -2.4080 |
| sortino_ratio | -0.7739 |
| max_drawdown | 0.5574 |
| cagr | -0.3057 |
| net_avg_win | 69.6284 |
| net_avg_loss | -95.9209 |
| avg_hold_time_bars | 11.1224 |
| exposure | 0.2579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
