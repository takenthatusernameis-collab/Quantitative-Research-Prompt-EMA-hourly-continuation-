# EMA Hourly Continuation — TRB/USDT P89_144

**Symbol:** TRB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.1083 |
| sortino_ratio | -0.5056 |
| max_drawdown | 0.4788 |
| cagr | -0.2073 |
| net_avg_win | 63.6047 |
| net_avg_loss | -89.0070 |
| avg_hold_time_bars | 6.9647 |
| exposure | 0.0892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
