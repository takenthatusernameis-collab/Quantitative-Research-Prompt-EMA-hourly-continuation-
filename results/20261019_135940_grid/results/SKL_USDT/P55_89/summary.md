# EMA Hourly Continuation — SKL/USDT P55_89

**Symbol:** SKL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.5755 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0023 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -4.4919 |
| sortino_ratio | -1.6557 |
| max_drawdown | 0.8663 |
| cagr | -0.5449 |
| net_avg_win | 35.0779 |
| net_avg_loss | -59.3456 |
| avg_hold_time_bars | 4.1348 |
| exposure | 0.1269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
