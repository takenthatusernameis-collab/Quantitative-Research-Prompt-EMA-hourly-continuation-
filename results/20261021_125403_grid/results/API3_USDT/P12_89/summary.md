# EMA Hourly Continuation — API3/USDT P12_89

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8772 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -2.4077 |
| sortino_ratio | -0.7914 |
| max_drawdown | 0.6219 |
| cagr | -0.3050 |
| net_avg_win | 60.4465 |
| net_avg_loss | -74.7747 |
| avg_hold_time_bars | 21.7790 |
| exposure | 0.5286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
