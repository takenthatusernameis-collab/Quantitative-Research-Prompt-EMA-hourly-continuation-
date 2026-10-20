# EMA Hourly Continuation — SUSHI/USDT P100_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.3547 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7479 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -6.1237 |
| sortino_ratio | -1.9576 |
| max_drawdown | 0.9145 |
| cagr | -0.6215 |
| net_avg_win | 23.0368 |
| net_avg_loss | -48.4923 |
| avg_hold_time_bars | 3.7137 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
