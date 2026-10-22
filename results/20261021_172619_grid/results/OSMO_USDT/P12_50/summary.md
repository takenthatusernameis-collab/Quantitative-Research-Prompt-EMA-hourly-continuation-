# EMA Hourly Continuation — OSMO/USDT P12_50

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.6903 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -3.8724 |
| sortino_ratio | -1.4292 |
| max_drawdown | 0.8154 |
| cagr | -0.4812 |
| net_avg_win | 58.8226 |
| net_avg_loss | -71.2452 |
| avg_hold_time_bars | 10.5060 |
| exposure | 0.3209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
