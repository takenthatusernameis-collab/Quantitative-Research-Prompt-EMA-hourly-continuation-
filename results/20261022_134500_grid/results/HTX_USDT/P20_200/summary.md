# EMA Hourly Continuation — HTX/USDT P20_200

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.3541 |
| net_win_rate | 0.3669 |
| gross_profit_factor | 0.8631 |
| gross_win_rate | 0.4362 |
| sharpe_ratio | -7.5159 |
| sortino_ratio | -2.2440 |
| max_drawdown | 0.9566 |
| cagr | -0.7088 |
| net_avg_win | 31.9446 |
| net_avg_loss | -52.2755 |
| avg_hold_time_bars | 32.3803 |
| exposure | 0.6550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
