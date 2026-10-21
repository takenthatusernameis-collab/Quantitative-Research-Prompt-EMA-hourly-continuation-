# EMA Hourly Continuation — FLOW/USDT P8_26

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.6168 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8723 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -3.8578 |
| sortino_ratio | -1.4989 |
| max_drawdown | 0.8376 |
| cagr | -0.4963 |
| net_avg_win | 37.9914 |
| net_avg_loss | -54.9586 |
| avg_hold_time_bars | 6.2209 |
| exposure | 0.2087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
