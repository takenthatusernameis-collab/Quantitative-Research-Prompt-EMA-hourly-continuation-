# EMA Hourly Continuation — ORCA/USDT P12_144

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.8131 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.1952 |
| sortino_ratio | -0.3384 |
| max_drawdown | 0.3739 |
| cagr | -0.1469 |
| net_avg_win | 71.9294 |
| net_avg_loss | -90.2803 |
| avg_hold_time_bars | 37.2259 |
| exposure | 0.6667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
