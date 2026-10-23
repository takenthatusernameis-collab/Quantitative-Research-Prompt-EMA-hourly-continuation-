# EMA Hourly Continuation — MTL/USDT P12_21

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1367 |
| net_profit_factor | 0.3252 |
| net_win_rate | 0.3943 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -13.1906 |
| sortino_ratio | -6.9904 |
| max_drawdown | 0.9999 |
| cagr | -0.9718 |
| net_avg_win | 8.9418 |
| net_avg_loss | -17.8966 |
| avg_hold_time_bars | 3.2173 |
| exposure | 0.1990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
