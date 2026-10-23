# EMA Hourly Continuation — FIDA/USDT P21_144

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.5773 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -3.8767 |
| sortino_ratio | -1.2566 |
| max_drawdown | 0.7876 |
| cagr | -0.4493 |
| net_avg_win | 44.2784 |
| net_avg_loss | -63.2534 |
| avg_hold_time_bars | 22.5367 |
| exposure | 0.5415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
