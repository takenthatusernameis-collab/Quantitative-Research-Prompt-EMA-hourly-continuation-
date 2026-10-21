# EMA Hourly Continuation — XCN/USDT P12_200

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.6916 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8253 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -2.2036 |
| sortino_ratio | -0.5872 |
| max_drawdown | 0.4955 |
| cagr | -0.2380 |
| net_avg_win | 68.9097 |
| net_avg_loss | -82.6886 |
| avg_hold_time_bars | 42.2986 |
| exposure | 0.6825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
