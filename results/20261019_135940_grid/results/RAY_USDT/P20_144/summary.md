# EMA Hourly Continuation — RAY/USDT P20_144

**Symbol:** RAY/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.6733 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9041 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -2.8132 |
| sortino_ratio | -0.8891 |
| max_drawdown | 0.6733 |
| cagr | -0.3428 |
| net_avg_win | 56.6617 |
| net_avg_loss | -74.9752 |
| avg_hold_time_bars | 22.1193 |
| exposure | 0.5057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
