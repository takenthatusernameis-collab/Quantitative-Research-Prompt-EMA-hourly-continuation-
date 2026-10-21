# EMA Hourly Continuation — ATH/USDT P12_50

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.9034 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1262 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -0.7450 |
| sortino_ratio | -0.2632 |
| max_drawdown | 0.3471 |
| cagr | -0.1194 |
| net_avg_win | 81.1759 |
| net_avg_loss | -101.4324 |
| avg_hold_time_bars | 10.3452 |
| exposure | 0.2818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
