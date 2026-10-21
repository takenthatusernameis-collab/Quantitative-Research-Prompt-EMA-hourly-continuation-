# EMA Hourly Continuation — XNO/USDT P20_89

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.6592 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8279 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -3.2875 |
| sortino_ratio | -1.0797 |
| max_drawdown | 0.7271 |
| cagr | -0.3918 |
| net_avg_win | 57.7226 |
| net_avg_loss | -70.4611 |
| avg_hold_time_bars | 13.8190 |
| exposure | 0.3367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
