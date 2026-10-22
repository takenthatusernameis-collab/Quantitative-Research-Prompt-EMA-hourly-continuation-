# EMA Hourly Continuation — INJ/USDT P8_20

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1696 |
| net_profit_factor | 0.4346 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8325 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -11.2356 |
| sortino_ratio | -6.4756 |
| max_drawdown | 0.9998 |
| cagr | -0.9636 |
| net_avg_win | 10.2589 |
| net_avg_loss | -18.6710 |
| avg_hold_time_bars | 2.8331 |
| exposure | 0.2184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
