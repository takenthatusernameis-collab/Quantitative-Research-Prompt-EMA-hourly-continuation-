# EMA Hourly Continuation — OP/USDT P50_144

**Symbol:** OP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7466 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9328 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -1.7485 |
| sortino_ratio | -0.4446 |
| max_drawdown | 0.4451 |
| cagr | -0.1846 |
| net_avg_win | 77.7115 |
| net_avg_loss | -95.3133 |
| avg_hold_time_bars | 21.0063 |
| exposure | 0.3036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
