# EMA Hourly Continuation — STRAX/USDT P20_21

**Symbol:** STRAX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1223 |
| net_profit_factor | 0.2002 |
| net_win_rate | 0.2886 |
| gross_profit_factor | 0.7114 |
| gross_win_rate | 0.3810 |
| sharpe_ratio | -17.3909 |
| sortino_ratio | -9.0836 |
| max_drawdown | 1.0000 |
| cagr | -0.9932 |
| net_avg_win | 7.0915 |
| net_avg_loss | -14.3716 |
| avg_hold_time_bars | 2.9624 |
| exposure | 0.1656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
