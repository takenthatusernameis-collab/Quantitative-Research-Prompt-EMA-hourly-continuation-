# EMA Hourly Continuation — MLK/USDT P8_55

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.3140 |
| net_win_rate | 0.3060 |
| gross_profit_factor | 0.6151 |
| gross_win_rate | 0.3188 |
| sharpe_ratio | -14.5666 |
| sortino_ratio | -7.5742 |
| max_drawdown | 0.9999 |
| cagr | -0.9780 |
| net_avg_win | 11.2458 |
| net_avg_loss | -15.7924 |
| avg_hold_time_bars | 7.6940 |
| exposure | 0.4631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
