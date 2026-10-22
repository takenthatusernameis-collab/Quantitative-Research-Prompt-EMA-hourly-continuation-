# EMA Hourly Continuation — XCN/USDT P20_89

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.4639 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.7999 |
| gross_win_rate | 0.4287 |
| sharpe_ratio | -7.9787 |
| sortino_ratio | -3.3534 |
| max_drawdown | 0.9858 |
| cagr | -0.8148 |
| net_avg_win | 22.9286 |
| net_avg_loss | -34.4928 |
| avg_hold_time_bars | 9.3028 |
| exposure | 0.3827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
