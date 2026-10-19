# EMA Hourly Continuation — DOGE/USDT P26_34

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.2120 |
| net_win_rate | 0.3569 |
| gross_profit_factor | 0.6688 |
| gross_win_rate | 0.4163 |
| sharpe_ratio | -13.6884 |
| sortino_ratio | -6.4583 |
| max_drawdown | 0.9998 |
| cagr | -0.9695 |
| net_avg_win | 7.2105 |
| net_avg_loss | -18.8809 |
| avg_hold_time_bars | 2.0766 |
| exposure | 0.0986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
