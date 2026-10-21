# EMA Hourly Continuation — WAVES/USDT P8_21

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -3.5902 |
| sortino_ratio | -1.2154 |
| max_drawdown | 0.7601 |
| cagr | -0.4275 |
| net_avg_win | 46.6996 |
| net_avg_loss | -70.1912 |
| avg_hold_time_bars | 5.9390 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
