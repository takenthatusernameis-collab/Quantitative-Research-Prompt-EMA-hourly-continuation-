# EMA Hourly Continuation — NMR/USDT P8_55

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.6306 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 1.0109 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -5.8805 |
| sortino_ratio | -2.7919 |
| max_drawdown | 0.9680 |
| cagr | -0.7417 |
| net_avg_win | 30.2833 |
| net_avg_loss | -43.6905 |
| avg_hold_time_bars | 8.9292 |
| exposure | 0.4643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
