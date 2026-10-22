# EMA Hourly Continuation — XAI/USDT P21_26

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.5312 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.7283 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -2.9245 |
| sortino_ratio | -0.6403 |
| max_drawdown | 0.5352 |
| cagr | -0.2546 |
| net_avg_win | 57.9873 |
| net_avg_loss | -82.4750 |
| avg_hold_time_bars | 4.5021 |
| exposure | 0.0485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
