# EMA Hourly Continuation — INJ/USDT P20_200

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.6407 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -2.5975 |
| sortino_ratio | -0.6484 |
| max_drawdown | 0.5606 |
| cagr | -0.2691 |
| net_avg_win | 66.5334 |
| net_avg_loss | -86.6418 |
| avg_hold_time_bars | 45.8629 |
| exposure | 0.6692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
