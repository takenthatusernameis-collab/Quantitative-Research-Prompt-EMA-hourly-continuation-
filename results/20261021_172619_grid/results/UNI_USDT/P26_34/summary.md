# EMA Hourly Continuation — UNI/USDT P26_34

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.7139 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 0.9914 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.1959 |
| sortino_ratio | -0.2113 |
| max_drawdown | 0.2439 |
| cagr | -0.0916 |
| net_avg_win | 70.3471 |
| net_avg_loss | -99.8539 |
| avg_hold_time_bars | 4.8808 |
| exposure | 0.0335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
