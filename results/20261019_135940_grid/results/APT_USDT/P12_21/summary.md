# EMA Hourly Continuation — APT/USDT P12_21

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1491 |
| net_profit_factor | 0.2087 |
| net_win_rate | 0.3883 |
| gross_profit_factor | 0.6123 |
| gross_win_rate | 0.4111 |
| sharpe_ratio | -14.4118 |
| sortino_ratio | -7.9298 |
| max_drawdown | 1.0000 |
| cagr | -0.9851 |
| net_avg_win | 4.5564 |
| net_avg_loss | -13.8573 |
| avg_hold_time_bars | 2.2193 |
| exposure | 0.1504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
