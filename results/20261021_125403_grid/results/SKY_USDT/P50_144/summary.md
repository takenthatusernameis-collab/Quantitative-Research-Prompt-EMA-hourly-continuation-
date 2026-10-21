# EMA Hourly Continuation — SKY/USDT P50_144

**Symbol:** SKY/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8769 |
| net_win_rate | 0.5325 |
| gross_profit_factor | 1.1330 |
| gross_win_rate | 0.5325 |
| sharpe_ratio | -0.7994 |
| sortino_ratio | -0.2241 |
| max_drawdown | 0.3554 |
| cagr | -0.1002 |
| net_avg_win | 84.4563 |
| net_avg_loss | -109.6845 |
| avg_hold_time_bars | 16.1266 |
| exposure | 0.2770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
