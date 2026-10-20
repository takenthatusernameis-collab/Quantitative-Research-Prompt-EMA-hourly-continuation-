# EMA Hourly Continuation — XEC/USDT P34_89

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.4955 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.8715 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -6.4267 |
| sortino_ratio | -2.4925 |
| max_drawdown | 0.9555 |
| cagr | -0.7051 |
| net_avg_win | 28.2251 |
| net_avg_loss | -43.6752 |
| avg_hold_time_bars | 7.5974 |
| exposure | 0.2630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
