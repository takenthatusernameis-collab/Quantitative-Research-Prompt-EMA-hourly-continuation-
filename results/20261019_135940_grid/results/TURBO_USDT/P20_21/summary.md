# EMA Hourly Continuation — TURBO/USDT P20_21

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1060 |
| net_profit_factor | 0.2480 |
| net_win_rate | 0.3047 |
| gross_profit_factor | 0.6440 |
| gross_win_rate | 0.3736 |
| sharpe_ratio | -17.0005 |
| sortino_ratio | -8.9997 |
| max_drawdown | 1.0000 |
| cagr | -0.9931 |
| net_avg_win | 10.2121 |
| net_avg_loss | -18.0437 |
| avg_hold_time_bars | 1.6745 |
| exposure | 0.0968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
