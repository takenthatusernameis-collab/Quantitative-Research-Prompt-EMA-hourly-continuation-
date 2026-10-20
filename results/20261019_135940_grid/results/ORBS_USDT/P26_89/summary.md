# EMA Hourly Continuation — ORBS/USDT P26_89

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5600 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -6.3920 |
| sortino_ratio | -2.4491 |
| max_drawdown | 0.9543 |
| cagr | -0.6994 |
| net_avg_win | 37.3615 |
| net_avg_loss | -51.9625 |
| avg_hold_time_bars | 10.9730 |
| exposure | 0.3691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
