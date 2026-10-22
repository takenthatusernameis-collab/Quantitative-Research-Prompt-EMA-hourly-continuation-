# EMA Hourly Continuation — ARPA/USDT P144_200

**Symbol:** ARPA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.5683 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8393 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -3.0905 |
| sortino_ratio | -0.7106 |
| max_drawdown | 0.5849 |
| cagr | -0.2803 |
| net_avg_win | 63.9878 |
| net_avg_loss | -90.7009 |
| avg_hold_time_bars | 7.3154 |
| exposure | 0.0861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
