# EMA Hourly Continuation — BTC/USDT P26_200

**Symbol:** BTC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5007 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -4.3643 |
| sortino_ratio | -1.1839 |
| max_drawdown | 0.8130 |
| cagr | -0.4443 |
| net_avg_win | 42.0325 |
| net_avg_loss | -70.1916 |
| avg_hold_time_bars | 32.1103 |
| exposure | 0.5472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
