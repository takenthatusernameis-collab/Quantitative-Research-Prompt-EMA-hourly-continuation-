# EMA Hourly Continuation — KNC/USDT P34_89

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7177 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0192 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -2.5795 |
| sortino_ratio | -0.8048 |
| max_drawdown | 0.6381 |
| cagr | -0.3084 |
| net_avg_win | 65.3463 |
| net_avg_loss | -89.5217 |
| avg_hold_time_bars | 11.5190 |
| exposure | 0.2482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
