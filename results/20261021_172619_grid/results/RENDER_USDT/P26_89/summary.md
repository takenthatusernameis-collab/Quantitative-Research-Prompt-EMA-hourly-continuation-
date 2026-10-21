# EMA Hourly Continuation — RENDER/USDT P26_89

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8291 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0257 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.2790 |
| sortino_ratio | -0.3931 |
| max_drawdown | 0.4173 |
| cagr | -0.1671 |
| net_avg_win | 78.8275 |
| net_avg_loss | -98.0057 |
| avg_hold_time_bars | 13.0505 |
| exposure | 0.2728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
