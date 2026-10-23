# EMA Hourly Continuation — ONT/USDT P12_144

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.5589 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8184 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -3.9070 |
| sortino_ratio | -1.2672 |
| max_drawdown | 0.7970 |
| cagr | -0.4611 |
| net_avg_win | 40.5152 |
| net_avg_loss | -59.6831 |
| avg_hold_time_bars | 25.3053 |
| exposure | 0.6264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
