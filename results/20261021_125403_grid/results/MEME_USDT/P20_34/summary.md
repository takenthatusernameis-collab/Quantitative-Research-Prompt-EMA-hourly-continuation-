# EMA Hourly Continuation — MEME/USDT P20_34

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6249 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.8643 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -2.9454 |
| sortino_ratio | -0.8203 |
| max_drawdown | 0.6212 |
| cagr | -0.3131 |
| net_avg_win | 57.7915 |
| net_avg_loss | -79.7889 |
| avg_hold_time_bars | 5.4132 |
| exposure | 0.0935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
