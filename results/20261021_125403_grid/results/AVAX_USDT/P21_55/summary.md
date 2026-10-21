# EMA Hourly Continuation — AVAX/USDT P21_55

**Symbol:** AVAX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6870 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9157 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.8812 |
| sortino_ratio | -0.8858 |
| max_drawdown | 0.6522 |
| cagr | -0.3337 |
| net_avg_win | 64.6715 |
| net_avg_loss | -82.6978 |
| avg_hold_time_bars | 8.4267 |
| exposure | 0.1777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
