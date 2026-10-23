# EMA Hourly Continuation — SLP/USDT P89_100

**Symbol:** SLP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.2708 |
| net_win_rate | 0.3744 |
| gross_profit_factor | 0.7822 |
| gross_win_rate | 0.4229 |
| sharpe_ratio | -10.1372 |
| sortino_ratio | -3.8250 |
| max_drawdown | 0.9939 |
| cagr | -0.8689 |
| net_avg_win | 14.4720 |
| net_avg_loss | -31.9941 |
| avg_hold_time_bars | 2.2335 |
| exposure | 0.0691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
