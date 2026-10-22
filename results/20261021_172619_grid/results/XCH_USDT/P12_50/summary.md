# EMA Hourly Continuation — XCH/USDT P12_50

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.7027 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.6092 |
| sortino_ratio | -0.9614 |
| max_drawdown | 0.6797 |
| cagr | -0.3573 |
| net_avg_win | 49.3609 |
| net_avg_loss | -65.5502 |
| avg_hold_time_bars | 10.4586 |
| exposure | 0.3161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
