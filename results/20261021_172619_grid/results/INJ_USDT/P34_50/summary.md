# EMA Hourly Continuation — INJ/USDT P34_50

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.8376 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.1057 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -0.8561 |
| sortino_ratio | -0.1898 |
| max_drawdown | 0.2451 |
| cagr | -0.0842 |
| net_avg_win | 82.4448 |
| net_avg_loss | -108.9776 |
| avg_hold_time_bars | 5.3305 |
| exposure | 0.0572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
