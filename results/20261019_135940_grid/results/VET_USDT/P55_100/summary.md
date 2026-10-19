# EMA Hourly Continuation — VET/USDT P55_100

**Symbol:** VET/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.5546 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0375 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -4.2373 |
| sortino_ratio | -1.5251 |
| max_drawdown | 0.8425 |
| cagr | -0.5137 |
| net_avg_win | 32.3376 |
| net_avg_loss | -59.2321 |
| avg_hold_time_bars | 4.9828 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
