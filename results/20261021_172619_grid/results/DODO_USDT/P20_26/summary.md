# EMA Hourly Continuation — DODO/USDT P20_26

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.5725 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -3.1078 |
| sortino_ratio | -0.7880 |
| max_drawdown | 0.6006 |
| cagr | -0.3041 |
| net_avg_win | 56.1386 |
| net_avg_loss | -81.0482 |
| avg_hold_time_bars | 5.3703 |
| exposure | 0.0768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
