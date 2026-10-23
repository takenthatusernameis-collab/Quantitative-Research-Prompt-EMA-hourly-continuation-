# EMA Hourly Continuation — G/USDT P26_55

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.5341 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.9594 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -6.7236 |
| sortino_ratio | -2.7647 |
| max_drawdown | 0.9431 |
| cagr | -0.7329 |
| net_avg_win | 33.5774 |
| net_avg_loss | -50.8609 |
| avg_hold_time_bars | 6.1417 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
