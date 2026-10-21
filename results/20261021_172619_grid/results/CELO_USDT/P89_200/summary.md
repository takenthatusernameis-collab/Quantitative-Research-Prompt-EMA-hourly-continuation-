# EMA Hourly Continuation — CELO/USDT P89_200

**Symbol:** CELO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9590 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.5220 |
| sortino_ratio | -0.3572 |
| max_drawdown | 0.3598 |
| cagr | -0.1520 |
| net_avg_win | 78.9199 |
| net_avg_loss | -99.4240 |
| avg_hold_time_bars | 14.6642 |
| exposure | 0.1798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
