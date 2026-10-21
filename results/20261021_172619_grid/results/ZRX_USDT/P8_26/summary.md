# EMA Hourly Continuation — ZRX/USDT P8_26

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.6125 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.8699 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -4.7448 |
| sortino_ratio | -1.9808 |
| max_drawdown | 0.8989 |
| cagr | -0.5966 |
| net_avg_win | 35.7403 |
| net_avg_loss | -50.8025 |
| avg_hold_time_bars | 6.5744 |
| exposure | 0.2549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
