# EMA Hourly Continuation — KAVA/USDT P8_26

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 779 |
| net_profit_factor | 0.6669 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9989 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -4.5081 |
| sortino_ratio | -1.7976 |
| max_drawdown | 0.8801 |
| cagr | -0.5672 |
| net_avg_win | 47.1295 |
| net_avg_loss | -64.9221 |
| avg_hold_time_bars | 6.9474 |
| exposure | 0.2460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
