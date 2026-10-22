# EMA Hourly Continuation — TRX/USDT P50_144

**Symbol:** TRX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.3392 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -7.0199 |
| sortino_ratio | -2.0952 |
| max_drawdown | 0.9374 |
| cagr | -0.6665 |
| net_avg_win | 25.9884 |
| net_avg_loss | -55.3651 |
| avg_hold_time_bars | 11.9932 |
| exposure | 0.2404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
