# EMA Hourly Continuation — ETHFI/USDT P34_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.6194 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9497 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -4.4928 |
| sortino_ratio | -1.7083 |
| max_drawdown | 0.8786 |
| cagr | -0.5608 |
| net_avg_win | 41.3135 |
| net_avg_loss | -59.1377 |
| avg_hold_time_bars | 7.3757 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
