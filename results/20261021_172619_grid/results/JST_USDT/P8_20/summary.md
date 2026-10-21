# EMA Hourly Continuation — JST/USDT P8_20

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.4338 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0105 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -5.5551 |
| sortino_ratio | -2.0741 |
| max_drawdown | 0.9124 |
| cagr | -0.6138 |
| net_avg_win | 20.9855 |
| net_avg_loss | -48.6666 |
| avg_hold_time_bars | 5.6571 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
