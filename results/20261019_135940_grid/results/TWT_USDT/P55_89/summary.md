# EMA Hourly Continuation — TWT/USDT P55_89

**Symbol:** TWT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.3762 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.8864 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -7.9748 |
| sortino_ratio | -3.0411 |
| max_drawdown | 0.9788 |
| cagr | -0.7826 |
| net_avg_win | 19.2776 |
| net_avg_loss | -37.9716 |
| avg_hold_time_bars | 3.8651 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
