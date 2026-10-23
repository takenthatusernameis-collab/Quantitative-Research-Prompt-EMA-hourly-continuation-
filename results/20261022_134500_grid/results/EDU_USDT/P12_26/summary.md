# EMA Hourly Continuation — EDU/USDT P12_26

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1419 |
| net_profit_factor | 0.3917 |
| net_win_rate | 0.4186 |
| gross_profit_factor | 0.7344 |
| gross_win_rate | 0.4292 |
| sharpe_ratio | -10.2128 |
| sortino_ratio | -5.4453 |
| max_drawdown | 0.9987 |
| cagr | -0.9286 |
| net_avg_win | 10.8247 |
| net_avg_loss | -19.8994 |
| avg_hold_time_bars | 3.4665 |
| exposure | 0.2226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
