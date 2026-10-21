# EMA Hourly Continuation — DCR/USDT P8_21

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.5308 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.7984 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -4.6757 |
| sortino_ratio | -1.7325 |
| max_drawdown | 0.8691 |
| cagr | -0.5501 |
| net_avg_win | 32.0372 |
| net_avg_loss | -50.0537 |
| avg_hold_time_bars | 5.9615 |
| exposure | 0.1821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
