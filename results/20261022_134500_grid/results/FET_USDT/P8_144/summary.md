# EMA Hourly Continuation — FET/USDT P8_144

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.7181 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -2.4984 |
| sortino_ratio | -0.7472 |
| max_drawdown | 0.6100 |
| cagr | -0.3052 |
| net_avg_win | 68.4617 |
| net_avg_loss | -89.7010 |
| avg_hold_time_bars | 35.9522 |
| exposure | 0.7517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
