# EMA Hourly Continuation — ALPINE/USDT P12_144

**Symbol:** ALPINE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.6909 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9241 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -1.7733 |
| sortino_ratio | -0.4081 |
| max_drawdown | 0.4225 |
| cagr | -0.1735 |
| net_avg_win | 66.4309 |
| net_avg_loss | -89.8318 |
| avg_hold_time_bars | 66.4755 |
| exposure | 0.8007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
