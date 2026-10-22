# EMA Hourly Continuation — ENS/USDT P34_100

**Symbol:** ENS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.5639 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.8960 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -4.4784 |
| sortino_ratio | -1.6114 |
| max_drawdown | 0.8641 |
| cagr | -0.5408 |
| net_avg_win | 35.6871 |
| net_avg_loss | -57.2157 |
| avg_hold_time_bars | 9.8076 |
| exposure | 0.2920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
