# EMA Hourly Continuation — SQD/USDT P12_89

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.7021 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -3.2181 |
| sortino_ratio | -1.2780 |
| max_drawdown | 0.7814 |
| cagr | -0.4566 |
| net_avg_win | 48.2974 |
| net_avg_loss | -65.6573 |
| avg_hold_time_bars | 12.9754 |
| exposure | 0.4708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
