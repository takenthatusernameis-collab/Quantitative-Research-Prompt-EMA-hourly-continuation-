# EMA Hourly Continuation — ONT/USDT P26_34

**Symbol:** ONT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.6405 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9659 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.0833 |
| sortino_ratio | -0.4532 |
| max_drawdown | 0.4431 |
| cagr | -0.1879 |
| net_avg_win | 63.8554 |
| net_avg_loss | -97.1373 |
| avg_hold_time_bars | 5.4242 |
| exposure | 0.0567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
