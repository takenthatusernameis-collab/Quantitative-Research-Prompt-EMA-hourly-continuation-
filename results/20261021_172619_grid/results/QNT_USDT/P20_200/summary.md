# EMA Hourly Continuation — QNT/USDT P20_200

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.8018 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9995 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3606 |
| sortino_ratio | -0.3790 |
| max_drawdown | 0.4073 |
| cagr | -0.1604 |
| net_avg_win | 76.0333 |
| net_avg_loss | -94.8320 |
| avg_hold_time_bars | 34.9709 |
| exposure | 0.6009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
