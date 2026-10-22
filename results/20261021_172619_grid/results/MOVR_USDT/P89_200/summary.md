# EMA Hourly Continuation — MOVR/USDT P89_200

**Symbol:** MOVR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7116 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.8900 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -1.7409 |
| sortino_ratio | -0.4274 |
| max_drawdown | 0.4099 |
| cagr | -0.1787 |
| net_avg_win | 68.2588 |
| net_avg_loss | -86.7030 |
| avg_hold_time_bars | 15.2727 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
