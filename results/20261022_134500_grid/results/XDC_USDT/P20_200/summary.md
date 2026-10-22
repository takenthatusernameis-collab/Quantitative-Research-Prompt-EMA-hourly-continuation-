# EMA Hourly Continuation — XDC/USDT P20_200

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5544 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9258 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -3.9308 |
| sortino_ratio | -1.2151 |
| max_drawdown | 0.7753 |
| cagr | -0.4461 |
| net_avg_win | 42.5584 |
| net_avg_loss | -66.9894 |
| avg_hold_time_bars | 26.1649 |
| exposure | 0.5768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
