# EMA Hourly Continuation — BLZ/USDT P34_89

**Symbol:** BLZ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.5139 |
| net_win_rate | 0.4019 |
| gross_profit_factor | 0.8143 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -7.0894 |
| sortino_ratio | -2.7202 |
| max_drawdown | 0.9628 |
| cagr | -0.7268 |
| net_avg_win | 34.2495 |
| net_avg_loss | -44.7812 |
| avg_hold_time_bars | 8.3126 |
| exposure | 0.2780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
