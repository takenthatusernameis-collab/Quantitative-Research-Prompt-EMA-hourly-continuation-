# EMA Hourly Continuation — T/USDT P34_55

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.4193 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.8531 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -7.6957 |
| sortino_ratio | -2.9408 |
| max_drawdown | 0.9761 |
| cagr | -0.7716 |
| net_avg_win | 22.2976 |
| net_avg_loss | -40.3966 |
| avg_hold_time_bars | 5.0423 |
| exposure | 0.1670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
