# EMA Hourly Continuation — IOTA/USDT P26_34

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.8251 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -2.5313 |
| sortino_ratio | -0.5431 |
| max_drawdown | 0.4827 |
| cagr | -0.2202 |
| net_avg_win | 59.2113 |
| net_avg_loss | -88.0668 |
| avg_hold_time_bars | 4.5822 |
| exposure | 0.0469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
