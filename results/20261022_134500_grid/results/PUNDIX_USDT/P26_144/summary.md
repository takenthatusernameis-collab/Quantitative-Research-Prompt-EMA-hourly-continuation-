# EMA Hourly Continuation — PUNDIX/USDT P26_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5934 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 0.8964 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -3.5235 |
| sortino_ratio | -1.1165 |
| max_drawdown | 0.7449 |
| cagr | -0.4179 |
| net_avg_win | 44.4386 |
| net_avg_loss | -68.6971 |
| avg_hold_time_bars | 21.8196 |
| exposure | 0.5058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
