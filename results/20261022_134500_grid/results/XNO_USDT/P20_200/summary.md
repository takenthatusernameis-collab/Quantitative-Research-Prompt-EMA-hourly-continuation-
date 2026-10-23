# EMA Hourly Continuation — XNO/USDT P20_200

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.5389 |
| net_win_rate | 0.4336 |
| gross_profit_factor | 0.7765 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -4.6344 |
| sortino_ratio | -1.5527 |
| max_drawdown | 0.8436 |
| cagr | -0.5223 |
| net_avg_win | 40.2470 |
| net_avg_loss | -57.1773 |
| avg_hold_time_bars | 22.6743 |
| exposure | 0.5823 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
