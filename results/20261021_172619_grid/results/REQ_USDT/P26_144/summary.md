# EMA Hourly Continuation — REQ/USDT P26_144

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6317 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8713 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -3.4222 |
| sortino_ratio | -1.0519 |
| max_drawdown | 0.7128 |
| cagr | -0.3856 |
| net_avg_win | 56.5621 |
| net_avg_loss | -76.0389 |
| avg_hold_time_bars | 20.4442 |
| exposure | 0.4330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
