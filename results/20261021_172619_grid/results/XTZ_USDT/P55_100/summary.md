# EMA Hourly Continuation — XTZ/USDT P55_100

**Symbol:** XTZ/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.7144 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0364 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -2.0263 |
| sortino_ratio | -0.5782 |
| max_drawdown | 0.4923 |
| cagr | -0.2313 |
| net_avg_win | 60.4416 |
| net_avg_loss | -88.1360 |
| avg_hold_time_bars | 7.9847 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
