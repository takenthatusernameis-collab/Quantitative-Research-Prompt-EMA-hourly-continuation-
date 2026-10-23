# EMA Hourly Continuation — WAVES/USDT P12_21

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1604 |
| net_profit_factor | 0.2731 |
| net_win_rate | 0.3641 |
| gross_profit_factor | 0.8679 |
| gross_win_rate | 0.4258 |
| sharpe_ratio | -16.4529 |
| sortino_ratio | -9.5261 |
| max_drawdown | 1.0000 |
| cagr | -0.9937 |
| net_avg_win | 6.4322 |
| net_avg_loss | -13.4866 |
| avg_hold_time_bars | 2.5112 |
| exposure | 0.1831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
