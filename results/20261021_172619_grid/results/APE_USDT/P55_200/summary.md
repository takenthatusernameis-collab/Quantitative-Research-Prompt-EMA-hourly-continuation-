# EMA Hourly Continuation — APE/USDT P55_200

**Symbol:** APE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7962 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9574 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.1062 |
| sortino_ratio | -0.2726 |
| max_drawdown | 0.3120 |
| cagr | -0.1193 |
| net_avg_win | 72.5889 |
| net_avg_loss | -89.3425 |
| avg_hold_time_bars | 26.1212 |
| exposure | 0.3526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
