# EMA Hourly Continuation — OGN/USDT P89_200

**Symbol:** OGN/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.4655 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.7140 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -4.6297 |
| sortino_ratio | -1.3548 |
| max_drawdown | 0.8237 |
| cagr | -0.4783 |
| net_avg_win | 38.1639 |
| net_avg_loss | -60.3413 |
| avg_hold_time_bars | 10.5253 |
| exposure | 0.2067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
