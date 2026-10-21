# EMA Hourly Continuation — GTC/USDT P26_144

**Symbol:** GTC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7233 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -2.1239 |
| sortino_ratio | -0.6045 |
| max_drawdown | 0.5494 |
| cagr | -0.2425 |
| net_avg_win | 70.2085 |
| net_avg_loss | -84.8194 |
| avg_hold_time_bars | 24.7406 |
| exposure | 0.4510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
