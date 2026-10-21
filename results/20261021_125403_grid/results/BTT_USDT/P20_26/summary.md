# EMA Hourly Continuation — BTT/USDT P20_26

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.3536 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.7331 |
| gross_win_rate | 0.3990 |
| sharpe_ratio | -4.9418 |
| sortino_ratio | -1.0480 |
| max_drawdown | 0.7143 |
| cagr | -0.3917 |
| net_avg_win | 47.5743 |
| net_avg_loss | -87.5511 |
| avg_hold_time_bars | 5.2837 |
| exposure | 0.0500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
