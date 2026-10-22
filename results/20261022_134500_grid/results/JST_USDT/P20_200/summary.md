# EMA Hourly Continuation — JST/USDT P20_200

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.4851 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9874 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -3.5856 |
| sortino_ratio | -0.9648 |
| max_drawdown | 0.7371 |
| cagr | -0.3946 |
| net_avg_win | 35.9879 |
| net_avg_loss | -69.3814 |
| avg_hold_time_bars | 33.7224 |
| exposure | 0.5936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
