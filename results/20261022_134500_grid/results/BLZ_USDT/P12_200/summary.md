# EMA Hourly Continuation — BLZ/USDT P12_200

**Symbol:** BLZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.8591 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -3.3235 |
| sortino_ratio | -1.0191 |
| max_drawdown | 0.7272 |
| cagr | -0.3845 |
| net_avg_win | 56.5790 |
| net_avg_loss | -74.4559 |
| avg_hold_time_bars | 32.7925 |
| exposure | 0.7153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
