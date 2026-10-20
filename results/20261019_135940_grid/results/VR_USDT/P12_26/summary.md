# EMA Hourly Continuation — VR/USDT P12_26

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1407 |
| net_profit_factor | 0.3583 |
| net_win_rate | 0.3014 |
| gross_profit_factor | 0.6666 |
| gross_win_rate | 0.3298 |
| sharpe_ratio | -17.6903 |
| sortino_ratio | -9.6164 |
| max_drawdown | 1.0000 |
| cagr | -0.9961 |
| net_avg_win | 13.1678 |
| net_avg_loss | -15.8526 |
| avg_hold_time_bars | 3.6063 |
| exposure | 0.2306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
