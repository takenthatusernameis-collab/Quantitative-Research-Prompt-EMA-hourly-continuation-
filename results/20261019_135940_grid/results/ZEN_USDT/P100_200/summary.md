# EMA Hourly Continuation — ZEN/USDT P100_200

**Symbol:** ZEN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.5296 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8566 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -3.8156 |
| sortino_ratio | -1.1045 |
| max_drawdown | 0.7507 |
| cagr | -0.4165 |
| net_avg_win | 42.5880 |
| net_avg_loss | -68.2332 |
| avg_hold_time_bars | 7.9602 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
