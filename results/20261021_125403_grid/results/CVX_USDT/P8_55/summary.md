# EMA Hourly Continuation — CVX/USDT P8_55

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 706 |
| net_profit_factor | 0.8157 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.6146 |
| sortino_ratio | -0.6145 |
| max_drawdown | 0.5222 |
| cagr | -0.2484 |
| net_avg_win | 63.8182 |
| net_avg_loss | -79.1282 |
| avg_hold_time_bars | 14.7040 |
| exposure | 0.4719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
