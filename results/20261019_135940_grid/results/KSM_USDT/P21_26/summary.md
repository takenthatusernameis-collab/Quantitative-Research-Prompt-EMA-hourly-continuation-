# EMA Hourly Continuation — KSM/USDT P21_26

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1192 |
| net_profit_factor | 0.2417 |
| net_win_rate | 0.3515 |
| gross_profit_factor | 0.8434 |
| gross_win_rate | 0.4253 |
| sharpe_ratio | -14.6905 |
| sortino_ratio | -7.4240 |
| max_drawdown | 1.0000 |
| cagr | -0.9808 |
| net_avg_win | 7.6087 |
| net_avg_loss | -17.0602 |
| avg_hold_time_bars | 1.9656 |
| exposure | 0.1065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
