# EMA Hourly Continuation — BLUR/USDT P12_144

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.8273 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.1353 |
| gross_win_rate | 0.5360 |
| sharpe_ratio | -1.1580 |
| sortino_ratio | -0.3422 |
| max_drawdown | 0.3797 |
| cagr | -0.1511 |
| net_avg_win | 71.1238 |
| net_avg_loss | -96.5549 |
| avg_hold_time_bars | 37.3828 |
| exposure | 0.7291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
