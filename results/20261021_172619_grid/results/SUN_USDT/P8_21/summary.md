# EMA Hourly Continuation — SUN/USDT P8_21

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.4440 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -7.5227 |
| sortino_ratio | -2.8998 |
| max_drawdown | 0.9708 |
| cagr | -0.7527 |
| net_avg_win | 23.7735 |
| net_avg_loss | -44.5294 |
| avg_hold_time_bars | 6.9081 |
| exposure | 0.2245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
