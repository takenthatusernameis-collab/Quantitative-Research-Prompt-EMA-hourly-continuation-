# EMA Hourly Continuation — BCH/USDT P20_34

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1135 |
| net_profit_factor | 0.2376 |
| net_win_rate | 0.3665 |
| gross_profit_factor | 0.6799 |
| gross_win_rate | 0.4150 |
| sharpe_ratio | -13.5435 |
| sortino_ratio | -6.5919 |
| max_drawdown | 0.9998 |
| cagr | -0.9696 |
| net_avg_win | 7.4896 |
| net_avg_loss | -18.2394 |
| avg_hold_time_bars | 2.6960 |
| exposure | 0.1391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
