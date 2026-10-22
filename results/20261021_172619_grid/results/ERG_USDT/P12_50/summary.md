# EMA Hourly Continuation — ERG/USDT P12_50

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -3.5803 |
| sortino_ratio | -1.2147 |
| max_drawdown | 0.7576 |
| cagr | -0.4291 |
| net_avg_win | 50.8534 |
| net_avg_loss | -65.7247 |
| avg_hold_time_bars | 10.9086 |
| exposure | 0.2821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
