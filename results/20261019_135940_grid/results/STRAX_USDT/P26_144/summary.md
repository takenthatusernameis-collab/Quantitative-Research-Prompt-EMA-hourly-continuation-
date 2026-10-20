# EMA Hourly Continuation — STRAX/USDT P26_144

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.5463 |
| net_win_rate | 0.4080 |
| gross_profit_factor | 0.7930 |
| gross_win_rate | 0.4139 |
| sharpe_ratio | -6.2613 |
| sortino_ratio | -2.2832 |
| max_drawdown | 0.9388 |
| cagr | -0.6712 |
| net_avg_win | 41.0602 |
| net_avg_loss | -51.8027 |
| avg_hold_time_bars | 13.8398 |
| exposure | 0.4265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
