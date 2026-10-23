# EMA Hourly Continuation — SLP/USDT P12_144

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6321 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9369 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -4.0377 |
| sortino_ratio | -1.3943 |
| max_drawdown | 0.8244 |
| cagr | -0.4912 |
| net_avg_win | 49.9358 |
| net_avg_loss | -67.4762 |
| avg_hold_time_bars | 23.7754 |
| exposure | 0.6592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
