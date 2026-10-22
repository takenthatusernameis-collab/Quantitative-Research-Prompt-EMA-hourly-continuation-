# EMA Hourly Continuation — XTZ/USDT P55_200

**Symbol:** XTZ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.6254 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -3.0170 |
| sortino_ratio | -0.8723 |
| max_drawdown | 0.6682 |
| cagr | -0.3401 |
| net_avg_win | 53.2903 |
| net_avg_loss | -79.7091 |
| avg_hold_time_bars | 19.8524 |
| exposure | 0.3790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
