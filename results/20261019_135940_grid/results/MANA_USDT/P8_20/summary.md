# EMA Hourly Continuation — MANA/USDT P8_20

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1691 |
| net_profit_factor | 0.3075 |
| net_win_rate | 0.4051 |
| gross_profit_factor | 0.8363 |
| gross_win_rate | 0.4364 |
| sharpe_ratio | -13.9157 |
| sortino_ratio | -8.1239 |
| max_drawdown | 1.0000 |
| cagr | -0.9845 |
| net_avg_win | 6.4822 |
| net_avg_loss | -14.3539 |
| avg_hold_time_bars | 2.7185 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
