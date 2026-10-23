# EMA Hourly Continuation — IO/USDT P21_50

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.5966 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.9187 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -5.9920 |
| sortino_ratio | -2.6676 |
| max_drawdown | 0.9518 |
| cagr | -0.7221 |
| net_avg_win | 32.9411 |
| net_avg_loss | -46.6881 |
| avg_hold_time_bars | 4.4657 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
