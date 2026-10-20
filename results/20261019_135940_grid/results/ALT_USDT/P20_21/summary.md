# EMA Hourly Continuation — ALT/USDT P20_21

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.2114 |
| net_win_rate | 0.3439 |
| gross_profit_factor | 0.7484 |
| gross_win_rate | 0.4095 |
| sharpe_ratio | -13.5193 |
| sortino_ratio | -6.2267 |
| max_drawdown | 0.9998 |
| cagr | -0.9672 |
| net_avg_win | 7.7452 |
| net_avg_loss | -19.2090 |
| avg_hold_time_bars | 2.8290 |
| exposure | 0.1294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
