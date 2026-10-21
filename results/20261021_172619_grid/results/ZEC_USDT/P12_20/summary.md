# EMA Hourly Continuation — ZEC/USDT P12_20

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8907 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -1.8472 |
| sortino_ratio | -0.4036 |
| max_drawdown | 0.3747 |
| cagr | -0.1691 |
| net_avg_win | 67.5020 |
| net_avg_loss | -91.1560 |
| avg_hold_time_bars | 5.1709 |
| exposure | 0.0550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
