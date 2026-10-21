# EMA Hourly Continuation — DIA/USDT P50_55

**Symbol:** DIA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.5777 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -2.3900 |
| sortino_ratio | -0.4630 |
| max_drawdown | 0.4533 |
| cagr | -0.1904 |
| net_avg_win | 66.4720 |
| net_avg_loss | -99.7987 |
| avg_hold_time_bars | 5.4426 |
| exposure | 0.0451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
