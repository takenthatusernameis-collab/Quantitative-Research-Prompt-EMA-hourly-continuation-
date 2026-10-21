# EMA Hourly Continuation — BSV/USDT P12_55

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6627 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8943 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.4029 |
| sortino_ratio | -1.2520 |
| max_drawdown | 0.7685 |
| cagr | -0.4362 |
| net_avg_win | 47.8928 |
| net_avg_loss | -64.2581 |
| avg_hold_time_bars | 11.0917 |
| exposure | 0.3353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
