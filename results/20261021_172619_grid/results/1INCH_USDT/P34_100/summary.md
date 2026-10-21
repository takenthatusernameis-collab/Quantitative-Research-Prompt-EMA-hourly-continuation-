# EMA Hourly Continuation — 1INCH/USDT P34_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7080 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.4035 |
| sortino_ratio | -0.7233 |
| max_drawdown | 0.5948 |
| cagr | -0.2829 |
| net_avg_win | 64.1715 |
| net_avg_loss | -84.6950 |
| avg_hold_time_bars | 14.4989 |
| exposure | 0.2920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
