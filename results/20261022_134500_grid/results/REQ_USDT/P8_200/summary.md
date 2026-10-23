# EMA Hourly Continuation — REQ/USDT P8_200

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.4442 |
| net_win_rate | 0.3836 |
| gross_profit_factor | 0.7551 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -7.6773 |
| sortino_ratio | -2.8765 |
| max_drawdown | 0.9718 |
| cagr | -0.7576 |
| net_avg_win | 28.5406 |
| net_avg_loss | -39.9964 |
| avg_hold_time_bars | 20.9154 |
| exposure | 0.6740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
