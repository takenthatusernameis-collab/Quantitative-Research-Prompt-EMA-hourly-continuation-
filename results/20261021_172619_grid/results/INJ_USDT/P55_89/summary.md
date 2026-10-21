# EMA Hourly Continuation — INJ/USDT P55_89

**Symbol:** INJ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.7657 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3416 |
| sortino_ratio | -0.3197 |
| max_drawdown | 0.3189 |
| cagr | -0.1366 |
| net_avg_win | 73.0401 |
| net_avg_loss | -95.3886 |
| avg_hold_time_bars | 6.4457 |
| exposure | 0.0809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
