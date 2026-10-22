# EMA Hourly Continuation — ZEC/USDT P55_100

**Symbol:** ZEC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.5528 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.9927 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -4.8373 |
| sortino_ratio | -1.7135 |
| max_drawdown | 0.8775 |
| cagr | -0.5611 |
| net_avg_win | 36.8468 |
| net_avg_loss | -57.4459 |
| avg_hold_time_bars | 4.4218 |
| exposure | 0.1272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
