# EMA Hourly Continuation — CELO/USDT P12_55

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.7405 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -2.5617 |
| sortino_ratio | -0.9417 |
| max_drawdown | 0.6739 |
| cagr | -0.3506 |
| net_avg_win | 58.6097 |
| net_avg_loss | -74.7534 |
| avg_hold_time_bars | 12.7669 |
| exposure | 0.3842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
