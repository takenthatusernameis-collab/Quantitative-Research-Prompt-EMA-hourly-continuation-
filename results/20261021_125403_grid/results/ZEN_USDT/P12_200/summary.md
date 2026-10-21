# EMA Hourly Continuation — ZEN/USDT P12_200

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 1.0183 |
| net_win_rate | 0.5415 |
| gross_profit_factor | 1.1773 |
| gross_win_rate | 0.5415 |
| sharpe_ratio | 0.1243 |
| sortino_ratio | 0.0258 |
| max_drawdown | 0.1168 |
| cagr | 0.0072 |
| net_avg_win | 90.5594 |
| net_avg_loss | -105.0119 |
| avg_hold_time_bars | 87.9415 |
| exposure | 0.8195 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
