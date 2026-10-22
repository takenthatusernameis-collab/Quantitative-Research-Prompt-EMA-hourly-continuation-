# EMA Hourly Continuation — BLZ/USDT P50_89

**Symbol:** BLZ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.4615 |
| net_win_rate | 0.3865 |
| gross_profit_factor | 0.8013 |
| gross_win_rate | 0.4044 |
| sharpe_ratio | -8.0837 |
| sortino_ratio | -3.0708 |
| max_drawdown | 0.9786 |
| cagr | -0.7790 |
| net_avg_win | 29.8169 |
| net_avg_loss | -40.7100 |
| avg_hold_time_bars | 6.1279 |
| exposure | 0.2016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
