# EMA Hourly Continuation — HTX/USDT P8_55

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.3089 |
| net_win_rate | 0.3392 |
| gross_profit_factor | 0.7746 |
| gross_win_rate | 0.3899 |
| sharpe_ratio | -14.0598 |
| sortino_ratio | -6.7189 |
| max_drawdown | 0.9999 |
| cagr | -0.9733 |
| net_avg_win | 12.1420 |
| net_avg_loss | -20.1774 |
| avg_hold_time_bars | 10.8276 |
| exposure | 0.5316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
