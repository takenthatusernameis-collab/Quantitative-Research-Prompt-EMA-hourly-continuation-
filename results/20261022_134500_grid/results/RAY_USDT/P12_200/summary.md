# EMA Hourly Continuation — RAY/USDT P12_200

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6510 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8749 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -3.0112 |
| sortino_ratio | -0.8792 |
| max_drawdown | 0.6773 |
| cagr | -0.3467 |
| net_avg_win | 61.2348 |
| net_avg_loss | -78.7169 |
| avg_hold_time_bars | 34.7426 |
| exposure | 0.6933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
