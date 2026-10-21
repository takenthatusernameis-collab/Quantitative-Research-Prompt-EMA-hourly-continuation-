# EMA Hourly Continuation — EGLD/USDT P8_50

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 737 |
| net_profit_factor | 0.8084 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0581 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -2.0711 |
| sortino_ratio | -0.8071 |
| max_drawdown | 0.6555 |
| cagr | -0.3103 |
| net_avg_win | 68.4346 |
| net_avg_loss | -87.2183 |
| avg_hold_time_bars | 12.7327 |
| exposure | 0.4265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
