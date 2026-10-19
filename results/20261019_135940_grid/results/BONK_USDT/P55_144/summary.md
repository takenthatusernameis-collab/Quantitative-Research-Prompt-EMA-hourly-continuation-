# EMA Hourly Continuation — BONK/USDT P55_144

**Symbol:** BONK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6729 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.7289 |
| sortino_ratio | -0.8408 |
| max_drawdown | 0.6483 |
| cagr | -0.3258 |
| net_avg_win | 56.2234 |
| net_avg_loss | -79.4052 |
| avg_hold_time_bars | 12.1250 |
| exposure | 0.2601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
