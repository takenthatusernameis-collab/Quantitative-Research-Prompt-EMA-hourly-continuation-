# EMA Hourly Continuation — BNB/USDT P89_144

**Symbol:** BNB/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.5702 |
| net_win_rate | 0.5345 |
| gross_profit_factor | 1.0859 |
| gross_win_rate | 0.5345 |
| sharpe_ratio | -2.5009 |
| sortino_ratio | -0.6021 |
| max_drawdown | 0.5110 |
| cagr | -0.2383 |
| net_avg_win | 44.6801 |
| net_avg_loss | -89.9945 |
| avg_hold_time_bars | 7.2109 |
| exposure | 0.0901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
