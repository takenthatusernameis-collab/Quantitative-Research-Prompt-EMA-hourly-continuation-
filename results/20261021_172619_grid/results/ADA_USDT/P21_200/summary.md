# EMA Hourly Continuation — ADA/USDT P21_200

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.8311 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0020 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -0.9349 |
| sortino_ratio | -0.2213 |
| max_drawdown | 0.2869 |
| cagr | -0.0984 |
| net_avg_win | 81.6958 |
| net_avg_loss | -99.7420 |
| avg_hold_time_bars | 49.0182 |
| exposure | 0.6105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
