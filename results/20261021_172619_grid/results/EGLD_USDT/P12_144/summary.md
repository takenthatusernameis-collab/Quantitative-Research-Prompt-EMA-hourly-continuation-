# EMA Hourly Continuation — EGLD/USDT P12_144

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.8634 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0583 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -0.8031 |
| sortino_ratio | -0.2229 |
| max_drawdown | 0.3592 |
| cagr | -0.1005 |
| net_avg_win | 76.4698 |
| net_avg_loss | -94.9638 |
| avg_hold_time_bars | 39.9035 |
| exposure | 0.6765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
