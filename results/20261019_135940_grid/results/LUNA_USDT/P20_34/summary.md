# EMA Hourly Continuation — LUNA/USDT P20_34

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1250 |
| net_profit_factor | 0.3381 |
| net_win_rate | 0.3880 |
| gross_profit_factor | 0.8140 |
| gross_win_rate | 0.4192 |
| sharpe_ratio | -12.9967 |
| sortino_ratio | -6.5986 |
| max_drawdown | 0.9998 |
| cagr | -0.9670 |
| net_avg_win | 10.5279 |
| net_avg_loss | -19.7439 |
| avg_hold_time_bars | 2.4000 |
| exposure | 0.1364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
