# EMA Hourly Continuation — API3/USDT P20_34

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6117 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -3.3505 |
| sortino_ratio | -0.9442 |
| max_drawdown | 0.6834 |
| cagr | -0.3528 |
| net_avg_win | 59.1613 |
| net_avg_loss | -80.7443 |
| avg_hold_time_bars | 5.1183 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
