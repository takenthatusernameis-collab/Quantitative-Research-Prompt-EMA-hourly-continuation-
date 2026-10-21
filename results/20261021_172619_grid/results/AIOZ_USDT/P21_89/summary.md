# EMA Hourly Continuation — AIOZ/USDT P21_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8027 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9684 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -1.5845 |
| sortino_ratio | -0.4875 |
| max_drawdown | 0.4908 |
| cagr | -0.2027 |
| net_avg_win | 77.3837 |
| net_avg_loss | -93.1415 |
| avg_hold_time_bars | 17.1164 |
| exposure | 0.3610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
