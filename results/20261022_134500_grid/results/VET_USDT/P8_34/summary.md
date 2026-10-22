# EMA Hourly Continuation — VET/USDT P8_34

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1399 |
| net_profit_factor | 0.5063 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.9373 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -9.0509 |
| sortino_ratio | -4.7561 |
| max_drawdown | 0.9974 |
| cagr | -0.9047 |
| net_avg_win | 16.3895 |
| net_avg_loss | -26.0641 |
| avg_hold_time_bars | 5.0322 |
| exposure | 0.3200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
