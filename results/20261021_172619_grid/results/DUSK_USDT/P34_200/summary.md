# EMA Hourly Continuation — DUSK/USDT P34_200

**Symbol:** DUSK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.8092 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.0440 |
| sortino_ratio | -0.2378 |
| max_drawdown | 0.3045 |
| cagr | -0.1049 |
| net_avg_win | 83.7263 |
| net_avg_loss | -95.6941 |
| avg_hold_time_bars | 46.0469 |
| exposure | 0.5358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
