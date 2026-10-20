# EMA Hourly Continuation — OSMO/USDT P100_144

**Symbol:** OSMO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 1.0285 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -4.1402 |
| sortino_ratio | -1.2370 |
| max_drawdown | 0.7800 |
| cagr | -0.4478 |
| net_avg_win | 40.1806 |
| net_avg_loss | -71.0776 |
| avg_hold_time_bars | 4.7725 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
