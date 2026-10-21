# EMA Hourly Continuation — ANYONE/USDT P34_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7688 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8802 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -1.4329 |
| sortino_ratio | -0.3688 |
| max_drawdown | 0.3551 |
| cagr | -0.1572 |
| net_avg_win | 76.6884 |
| net_avg_loss | -88.8754 |
| avg_hold_time_bars | 25.6068 |
| exposure | 0.3817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
