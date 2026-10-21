# EMA Hourly Continuation — XMR/USDT P144_200

**Symbol:** XMR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 145 |
| net_profit_factor | 0.5570 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.7777 |
| gross_win_rate | 0.4345 |
| sharpe_ratio | -2.1922 |
| sortino_ratio | -0.3761 |
| max_drawdown | 0.3974 |
| cagr | -0.1580 |
| net_avg_win | 69.9898 |
| net_avg_loss | -96.5416 |
| avg_hold_time_bars | 7.4621 |
| exposure | 0.0492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
