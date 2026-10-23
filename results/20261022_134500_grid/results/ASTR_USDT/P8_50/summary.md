# EMA Hourly Continuation — ASTR/USDT P8_50

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.6114 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 1.0368 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -5.0781 |
| sortino_ratio | -2.2462 |
| max_drawdown | 0.9352 |
| cagr | -0.6560 |
| net_avg_win | 30.8721 |
| net_avg_loss | -47.0323 |
| avg_hold_time_bars | 10.9898 |
| exposure | 0.4899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
