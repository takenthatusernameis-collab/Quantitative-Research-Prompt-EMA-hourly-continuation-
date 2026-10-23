# EMA Hourly Continuation — SKL/USDT P8_55

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.6889 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 1.0547 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -4.6965 |
| sortino_ratio | -2.1015 |
| max_drawdown | 0.9242 |
| cagr | -0.6340 |
| net_avg_win | 41.2270 |
| net_avg_loss | -57.1856 |
| avg_hold_time_bars | 11.2463 |
| exposure | 0.5168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
