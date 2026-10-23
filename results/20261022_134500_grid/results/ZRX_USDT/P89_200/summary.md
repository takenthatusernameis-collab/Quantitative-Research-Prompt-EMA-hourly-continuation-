# EMA Hourly Continuation — ZRX/USDT P89_200

**Symbol:** ZRX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.5691 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9065 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -3.6154 |
| sortino_ratio | -1.0469 |
| max_drawdown | 0.7327 |
| cagr | -0.4015 |
| net_avg_win | 47.5959 |
| net_avg_loss | -73.7343 |
| avg_hold_time_bars | 10.0186 |
| exposure | 0.1954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
