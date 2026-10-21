# EMA Hourly Continuation — ATH/USDT P21_200

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 1.1159 |
| net_win_rate | 0.5724 |
| gross_profit_factor | 1.3125 |
| gross_win_rate | 0.5724 |
| sharpe_ratio | 0.7065 |
| sortino_ratio | 0.1859 |
| max_drawdown | 0.1166 |
| cagr | 0.0762 |
| net_avg_win | 104.5006 |
| net_avg_loss | -125.3456 |
| avg_hold_time_bars | 39.9737 |
| exposure | 0.5890 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
