# EMA Hourly Continuation — ETC/USDT P21_100

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.5126 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9476 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -5.6834 |
| sortino_ratio | -2.0983 |
| max_drawdown | 0.9309 |
| cagr | -0.6477 |
| net_avg_win | 29.8155 |
| net_avg_loss | -51.2711 |
| avg_hold_time_bars | 11.8911 |
| exposure | 0.3773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
