# EMA Hourly Continuation — QNT/USDT P144_200

**Symbol:** QNT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.5654 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8294 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -2.5407 |
| sortino_ratio | -0.5241 |
| max_drawdown | 0.4614 |
| cagr | -0.2127 |
| net_avg_win | 62.4865 |
| net_avg_loss | -91.1255 |
| avg_hold_time_bars | 5.9087 |
| exposure | 0.0559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
