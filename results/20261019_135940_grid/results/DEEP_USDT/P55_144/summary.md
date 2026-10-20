# EMA Hourly Continuation — DEEP/USDT P55_144

**Symbol:** DEEP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6969 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.4167 |
| sortino_ratio | -0.7288 |
| max_drawdown | 0.5185 |
| cagr | -0.2937 |
| net_avg_win | 64.3757 |
| net_avg_loss | -88.4399 |
| avg_hold_time_bars | 10.6495 |
| exposure | 0.2219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
