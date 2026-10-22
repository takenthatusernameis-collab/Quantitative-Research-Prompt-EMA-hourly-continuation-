# EMA Hourly Continuation — ELON/USDT P34_55

**Symbol:** ELON/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.1799 |
| sortino_ratio | -0.4930 |
| max_drawdown | 0.4378 |
| cagr | -0.2023 |
| net_avg_win | 65.2548 |
| net_avg_loss | -93.0469 |
| avg_hold_time_bars | 6.1245 |
| exposure | 0.0693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
