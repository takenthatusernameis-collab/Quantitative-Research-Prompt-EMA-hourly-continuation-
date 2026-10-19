# EMA Hourly Continuation — HTX/USDT P34_100

**Symbol:** HTX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.2691 |
| net_win_rate | 0.2949 |
| gross_profit_factor | 0.7833 |
| gross_win_rate | 0.3675 |
| sharpe_ratio | -12.2291 |
| sortino_ratio | -4.7747 |
| max_drawdown | 0.9985 |
| cagr | -0.9232 |
| net_avg_win | 17.7546 |
| net_avg_loss | -27.5955 |
| avg_hold_time_bars | 10.0470 |
| exposure | 0.3192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
