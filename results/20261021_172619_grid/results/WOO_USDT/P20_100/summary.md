# EMA Hourly Continuation — WOO/USDT P20_100

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.7628 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.1098 |
| sortino_ratio | -0.6470 |
| max_drawdown | 0.5860 |
| cagr | -0.2585 |
| net_avg_win | 77.1860 |
| net_avg_loss | -91.2377 |
| avg_hold_time_bars | 20.3772 |
| exposure | 0.4298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
