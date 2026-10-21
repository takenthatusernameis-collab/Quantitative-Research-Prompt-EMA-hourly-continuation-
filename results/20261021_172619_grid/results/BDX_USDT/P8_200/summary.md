# EMA Hourly Continuation — BDX/USDT P8_200

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.4766 |
| net_win_rate | 0.4041 |
| gross_profit_factor | 0.7021 |
| gross_win_rate | 0.4041 |
| sharpe_ratio | -5.9249 |
| sortino_ratio | -2.0376 |
| max_drawdown | 0.9127 |
| cagr | -0.6158 |
| net_avg_win | 35.0853 |
| net_avg_loss | -49.9276 |
| avg_hold_time_bars | 18.0839 |
| exposure | 0.4800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
