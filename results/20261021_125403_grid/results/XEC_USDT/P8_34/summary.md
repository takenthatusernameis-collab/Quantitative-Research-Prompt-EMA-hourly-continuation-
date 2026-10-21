# EMA Hourly Continuation — XEC/USDT P8_34

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 850 |
| net_profit_factor | 0.6614 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9446 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -3.7812 |
| sortino_ratio | -1.5773 |
| max_drawdown | 0.8448 |
| cagr | -0.5123 |
| net_avg_win | 39.2844 |
| net_avg_loss | -56.9317 |
| avg_hold_time_bars | 8.2635 |
| exposure | 0.3178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
