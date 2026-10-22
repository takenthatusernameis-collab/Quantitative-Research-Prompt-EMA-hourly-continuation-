# EMA Hourly Continuation — TWT/USDT P12_20

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1595 |
| net_profit_factor | 0.2458 |
| net_win_rate | 0.3724 |
| gross_profit_factor | 0.7901 |
| gross_win_rate | 0.4445 |
| sharpe_ratio | -16.0086 |
| sortino_ratio | -9.2436 |
| max_drawdown | 1.0000 |
| cagr | -0.9924 |
| net_avg_win | 5.4866 |
| net_avg_loss | -13.2457 |
| avg_hold_time_bars | 2.2031 |
| exposure | 0.1597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
