# EMA Hourly Continuation — XNO/USDT P100_200

**Symbol:** XNO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8392 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -2.5728 |
| sortino_ratio | -0.6686 |
| max_drawdown | 0.5383 |
| cagr | -0.2649 |
| net_avg_win | 65.5724 |
| net_avg_loss | -83.5193 |
| avg_hold_time_bars | 10.8922 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
