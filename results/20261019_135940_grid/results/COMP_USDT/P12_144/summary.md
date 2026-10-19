# EMA Hourly Continuation — COMP/USDT P12_144

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6327 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 1.0003 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -2.9024 |
| sortino_ratio | -0.8993 |
| max_drawdown | 0.6724 |
| cagr | -0.3477 |
| net_avg_win | 47.4191 |
| net_avg_loss | -73.1169 |
| avg_hold_time_bars | 32.5806 |
| exposure | 0.7168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
