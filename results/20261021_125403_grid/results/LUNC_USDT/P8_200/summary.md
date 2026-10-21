# EMA Hourly Continuation — LUNC/USDT P8_200

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7100 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -1.8910 |
| sortino_ratio | -0.5072 |
| max_drawdown | 0.4667 |
| cagr | -0.2087 |
| net_avg_win | 64.3743 |
| net_avg_loss | -81.9451 |
| avg_hold_time_bars | 47.1770 |
| exposure | 0.7634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
