# EMA Hourly Continuation — MINA/USDT P8_200

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7517 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5182 |
| sharpe_ratio | -1.4798 |
| sortino_ratio | -0.3954 |
| max_drawdown | 0.4561 |
| cagr | -0.1723 |
| net_avg_win | 62.5541 |
| net_avg_loss | -87.5216 |
| avg_hold_time_bars | 49.9664 |
| exposure | 0.8108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
