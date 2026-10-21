# EMA Hourly Continuation — XDC/USDT P12_55

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.5768 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -4.1341 |
| sortino_ratio | -1.4014 |
| max_drawdown | 0.8020 |
| cagr | -0.4753 |
| net_avg_win | 42.2068 |
| net_avg_loss | -62.1360 |
| avg_hold_time_bars | 11.4291 |
| exposure | 0.2930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
