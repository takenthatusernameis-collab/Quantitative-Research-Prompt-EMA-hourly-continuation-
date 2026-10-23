# EMA Hourly Continuation — LUNA/USDT P50_89

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.3767 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.7786 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -8.0349 |
| sortino_ratio | -3.1261 |
| max_drawdown | 0.9830 |
| cagr | -0.8003 |
| net_avg_win | 17.9902 |
| net_avg_loss | -36.3176 |
| avg_hold_time_bars | 4.2709 |
| exposure | 0.1483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
