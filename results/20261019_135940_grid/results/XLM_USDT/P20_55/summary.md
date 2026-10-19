# EMA Hourly Continuation — XLM/USDT P20_55

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.3325 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -8.2168 |
| sortino_ratio | -3.6408 |
| max_drawdown | 0.9899 |
| cagr | -0.8388 |
| net_avg_win | 10.9788 |
| net_avg_loss | -27.3063 |
| avg_hold_time_bars | 5.4254 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
