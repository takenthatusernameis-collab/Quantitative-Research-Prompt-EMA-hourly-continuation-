# EMA Hourly Continuation — ETN/USDT P12_50

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5562 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.6993 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -4.3501 |
| sortino_ratio | -1.4517 |
| max_drawdown | 0.7605 |
| cagr | -0.4888 |
| net_avg_win | 48.8348 |
| net_avg_loss | -62.3914 |
| avg_hold_time_bars | 10.9872 |
| exposure | 0.2787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
