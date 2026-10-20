# EMA Hourly Continuation — MINA/USDT P89_144

**Symbol:** MINA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.4848 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8625 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -4.6023 |
| sortino_ratio | -1.4657 |
| max_drawdown | 0.8355 |
| cagr | -0.5054 |
| net_avg_win | 33.3479 |
| net_avg_loss | -60.0620 |
| avg_hold_time_bars | 5.6713 |
| exposure | 0.1294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
