# EMA Hourly Continuation — XNO/USDT P55_200

**Symbol:** XNO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6291 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -2.8723 |
| sortino_ratio | -0.7889 |
| max_drawdown | 0.5981 |
| cagr | -0.3044 |
| net_avg_win | 61.4728 |
| net_avg_loss | -76.4154 |
| avg_hold_time_bars | 18.2261 |
| exposure | 0.3115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
