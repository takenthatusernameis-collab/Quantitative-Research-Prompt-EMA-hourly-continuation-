# EMA Hourly Continuation — MNT/USDT P8_50

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7275 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 0.9837 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -2.4405 |
| sortino_ratio | -0.9109 |
| max_drawdown | 0.6574 |
| cagr | -0.3429 |
| net_avg_win | 51.1587 |
| net_avg_loss | -70.5304 |
| avg_hold_time_bars | 15.1605 |
| exposure | 0.4679 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
