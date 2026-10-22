# EMA Hourly Continuation — OSMO/USDT P12_144

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.8595 |
| net_win_rate | 0.5137 |
| gross_profit_factor | 1.0566 |
| gross_win_rate | 0.5137 |
| sharpe_ratio | -0.9701 |
| sortino_ratio | -0.2788 |
| max_drawdown | 0.3860 |
| cagr | -0.1230 |
| net_avg_win | 83.3746 |
| net_avg_loss | -102.4762 |
| avg_hold_time_bars | 35.2369 |
| exposure | 0.6423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
