# EMA Hourly Continuation — KAS/USDT P34_100

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.4306 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.7734 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -5.8460 |
| sortino_ratio | -2.1535 |
| max_drawdown | 0.9299 |
| cagr | -0.6515 |
| net_avg_win | 22.9644 |
| net_avg_loss | -43.1709 |
| avg_hold_time_bars | 7.3494 |
| exposure | 0.2285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
