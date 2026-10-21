# EMA Hourly Continuation — NYM/USDT P34_200

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.4712 |
| net_win_rate | 0.3985 |
| gross_profit_factor | 0.6500 |
| gross_win_rate | 0.4023 |
| sharpe_ratio | -3.5407 |
| sortino_ratio | -0.8150 |
| max_drawdown | 0.6269 |
| cagr | -0.3169 |
| net_avg_win | 51.7843 |
| net_avg_loss | -72.8088 |
| avg_hold_time_bars | 37.1203 |
| exposure | 0.4488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
