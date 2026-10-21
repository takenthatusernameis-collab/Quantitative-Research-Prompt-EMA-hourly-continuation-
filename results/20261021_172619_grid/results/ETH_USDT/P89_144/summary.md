# EMA Hourly Continuation — ETH/USDT P89_144

**Symbol:** ETH/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.5853 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.2114 |
| sortino_ratio | -0.4562 |
| max_drawdown | 0.4328 |
| cagr | -0.1886 |
| net_avg_win | 57.6156 |
| net_avg_loss | -92.8715 |
| avg_hold_time_bars | 9.2573 |
| exposure | 0.0867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
