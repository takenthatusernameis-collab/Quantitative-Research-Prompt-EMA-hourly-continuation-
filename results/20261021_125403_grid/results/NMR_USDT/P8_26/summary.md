# EMA Hourly Continuation — NMR/USDT P8_26

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.7480 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 1.0478 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -3.0556 |
| sortino_ratio | -1.2190 |
| max_drawdown | 0.7700 |
| cagr | -0.4284 |
| net_avg_win | 57.7221 |
| net_avg_loss | -77.7700 |
| avg_hold_time_bars | 5.8693 |
| exposure | 0.2062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
