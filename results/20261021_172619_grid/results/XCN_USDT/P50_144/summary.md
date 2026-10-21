# EMA Hourly Continuation — XCN/USDT P50_144

**Symbol:** XCN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7128 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9129 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.0802 |
| sortino_ratio | -0.5653 |
| max_drawdown | 0.4967 |
| cagr | -0.2289 |
| net_avg_win | 68.7656 |
| net_avg_loss | -87.3834 |
| avg_hold_time_bars | 16.2005 |
| exposure | 0.2680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
