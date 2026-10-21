# EMA Hourly Continuation — CARV/USDT P12_34

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9120 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -3.3038 |
| sortino_ratio | -1.2397 |
| max_drawdown | 0.6886 |
| cagr | -0.4334 |
| net_avg_win | 49.8823 |
| net_avg_loss | -70.1723 |
| avg_hold_time_bars | 7.8993 |
| exposure | 0.2472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
