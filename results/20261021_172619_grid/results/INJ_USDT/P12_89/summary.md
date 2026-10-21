# EMA Hourly Continuation — INJ/USDT P12_89

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.7835 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9283 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.7395 |
| sortino_ratio | -0.5562 |
| max_drawdown | 0.4796 |
| cagr | -0.2269 |
| net_avg_win | 71.1951 |
| net_avg_loss | -84.2488 |
| avg_hold_time_bars | 22.8310 |
| exposure | 0.5220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
