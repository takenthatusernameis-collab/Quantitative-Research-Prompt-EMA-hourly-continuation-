# EMA Hourly Continuation — ICP/USDT P8_55

**Symbol:** ICP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1141 |
| net_profit_factor | 0.5908 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.9492 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -6.1692 |
| sortino_ratio | -2.9128 |
| max_drawdown | 0.9737 |
| cagr | -0.7609 |
| net_avg_win | 25.8142 |
| net_avg_loss | -39.8121 |
| avg_hold_time_bars | 8.6985 |
| exposure | 0.4511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
