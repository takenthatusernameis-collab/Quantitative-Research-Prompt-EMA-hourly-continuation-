# EMA Hourly Continuation — AVA/USDT P20_200

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6086 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.8752 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.7998 |
| sortino_ratio | -0.8181 |
| max_drawdown | 0.6634 |
| cagr | -0.3288 |
| net_avg_win | 47.0688 |
| net_avg_loss | -70.2764 |
| avg_hold_time_bars | 28.4351 |
| exposure | 0.5674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
