# EMA Hourly Continuation — AIOZ/USDT P12_26

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -3.3496 |
| sortino_ratio | -0.9804 |
| max_drawdown | 0.7000 |
| cagr | -0.3629 |
| net_avg_win | 60.8135 |
| net_avg_loss | -75.6840 |
| avg_hold_time_bars | 5.6635 |
| exposure | 0.1094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
