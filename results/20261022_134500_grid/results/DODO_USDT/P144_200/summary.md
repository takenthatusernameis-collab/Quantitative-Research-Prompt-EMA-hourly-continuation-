# EMA Hourly Continuation — DODO/USDT P144_200

**Symbol:** DODO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.4206 |
| net_win_rate | 0.4080 |
| gross_profit_factor | 0.7368 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -5.7250 |
| sortino_ratio | -1.7680 |
| max_drawdown | 0.8815 |
| cagr | -0.5692 |
| net_avg_win | 33.1179 |
| net_avg_loss | -54.2734 |
| avg_hold_time_bars | 4.4524 |
| exposure | 0.0953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
