# EMA Hourly Continuation — BNB/USDT P50_144

**Symbol:** BNB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6293 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0296 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -2.6264 |
| sortino_ratio | -0.7373 |
| max_drawdown | 0.5811 |
| cagr | -0.2837 |
| net_avg_win | 49.6548 |
| net_avg_loss | -83.1906 |
| avg_hold_time_bars | 13.4365 |
| exposure | 0.2309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
