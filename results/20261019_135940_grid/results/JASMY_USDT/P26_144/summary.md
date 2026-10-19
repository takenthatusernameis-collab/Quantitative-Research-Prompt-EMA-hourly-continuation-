# EMA Hourly Continuation — JASMY/USDT P26_144

**Symbol:** JASMY/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.8114 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1302 |
| gross_win_rate | 0.5367 |
| sharpe_ratio | -1.3707 |
| sortino_ratio | -0.4425 |
| max_drawdown | 0.4851 |
| cagr | -0.1913 |
| net_avg_win | 64.6621 |
| net_avg_loss | -90.1866 |
| avg_hold_time_bars | 18.1100 |
| exposure | 0.4264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
