# EMA Hourly Continuation — KSM/USDT P20_26

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1216 |
| net_profit_factor | 0.2372 |
| net_win_rate | 0.3577 |
| gross_profit_factor | 0.7573 |
| gross_win_rate | 0.4235 |
| sharpe_ratio | -14.3929 |
| sortino_ratio | -7.3064 |
| max_drawdown | 0.9999 |
| cagr | -0.9790 |
| net_avg_win | 7.1465 |
| net_avg_loss | -16.7837 |
| avg_hold_time_bars | 2.0469 |
| exposure | 0.1131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
