# EMA Hourly Continuation — SSV/USDT P12_144

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6126 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8468 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -3.7449 |
| sortino_ratio | -1.1510 |
| max_drawdown | 0.7634 |
| cagr | -0.4197 |
| net_avg_win | 56.2253 |
| net_avg_loss | -71.6477 |
| avg_hold_time_bars | 32.3299 |
| exposure | 0.7008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
