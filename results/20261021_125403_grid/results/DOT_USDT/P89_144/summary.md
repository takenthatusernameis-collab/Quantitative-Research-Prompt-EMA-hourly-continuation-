# EMA Hourly Continuation — DOT/USDT P89_144

**Symbol:** DOT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7014 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9815 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -1.7491 |
| sortino_ratio | -0.3931 |
| max_drawdown | 0.4045 |
| cagr | -0.1646 |
| net_avg_win | 70.5483 |
| net_avg_loss | -98.1462 |
| avg_hold_time_bars | 6.5633 |
| exposure | 0.0731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
