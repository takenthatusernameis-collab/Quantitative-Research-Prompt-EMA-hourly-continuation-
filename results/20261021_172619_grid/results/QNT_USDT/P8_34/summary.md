# EMA Hourly Continuation — QNT/USDT P8_34

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.6884 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9674 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -3.2337 |
| sortino_ratio | -1.2711 |
| max_drawdown | 0.7748 |
| cagr | -0.4418 |
| net_avg_win | 45.7832 |
| net_avg_loss | -64.7578 |
| avg_hold_time_bars | 7.5465 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
