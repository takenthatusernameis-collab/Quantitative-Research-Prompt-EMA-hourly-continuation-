# EMA Hourly Continuation — AGLD/USDT P34_55

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.4358 |
| net_win_rate | 0.4268 |
| gross_profit_factor | 0.8276 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -7.7656 |
| sortino_ratio | -3.2450 |
| max_drawdown | 0.9825 |
| cagr | -0.7975 |
| net_avg_win | 20.1757 |
| net_avg_loss | -34.4713 |
| avg_hold_time_bars | 3.9523 |
| exposure | 0.1576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
