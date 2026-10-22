# EMA Hourly Continuation — ALGO/USDT P20_26

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1169 |
| net_profit_factor | 0.2101 |
| net_win_rate | 0.3798 |
| gross_profit_factor | 0.7075 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -13.6881 |
| sortino_ratio | -6.7676 |
| max_drawdown | 0.9999 |
| cagr | -0.9736 |
| net_avg_win | 5.9912 |
| net_avg_loss | -17.4607 |
| avg_hold_time_bars | 1.8229 |
| exposure | 0.0969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
