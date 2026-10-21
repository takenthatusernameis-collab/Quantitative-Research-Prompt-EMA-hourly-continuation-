# EMA Hourly Continuation — DUSK/USDT P26_144

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.9048 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0448 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -0.5334 |
| sortino_ratio | -0.1417 |
| max_drawdown | 0.2283 |
| cagr | -0.0666 |
| net_avg_win | 86.3105 |
| net_avg_loss | -99.9595 |
| avg_hold_time_bars | 29.2865 |
| exposure | 0.4553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
