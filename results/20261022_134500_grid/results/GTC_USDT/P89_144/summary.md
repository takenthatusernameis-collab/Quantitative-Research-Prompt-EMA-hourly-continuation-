# EMA Hourly Continuation — GTC/USDT P89_144

**Symbol:** GTC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.4917 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.8396 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -4.6102 |
| sortino_ratio | -1.4285 |
| max_drawdown | 0.8233 |
| cagr | -0.4910 |
| net_avg_win | 37.6200 |
| net_avg_loss | -60.1730 |
| avg_hold_time_bars | 6.0482 |
| exposure | 0.1311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
