# EMA Hourly Continuation — PEPE/USDT P144_200

**Symbol:** PEPE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 179 |
| net_profit_factor | 0.7830 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0029 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.0038 |
| sortino_ratio | -0.1927 |
| max_drawdown | 0.2268 |
| cagr | -0.0851 |
| net_avg_win | 80.2564 |
| net_avg_loss | -103.6464 |
| avg_hold_time_bars | 7.6313 |
| exposure | 0.0621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
