# EMA Hourly Continuation — MANA/USDT P34_200

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.8897 |
| net_win_rate | 0.5258 |
| gross_profit_factor | 1.0945 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -0.5827 |
| sortino_ratio | -0.1430 |
| max_drawdown | 0.2037 |
| cagr | -0.0665 |
| net_avg_win | 83.6532 |
| net_avg_loss | -104.2410 |
| avg_hold_time_bars | 41.6392 |
| exposure | 0.5508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
