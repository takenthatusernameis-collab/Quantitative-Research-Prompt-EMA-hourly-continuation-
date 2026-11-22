# EMA Hourly Continuation — AZERO/USDT P34_55

**Symbol:** AZERO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 737 |
| net_profit_factor | 0.3641 |
| net_win_rate | 0.4057 |
| gross_profit_factor | 0.7636 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -7.5169 |
| sortino_ratio | -2.8630 |
| max_drawdown | 0.9737 |
| cagr | -0.7625 |
| net_avg_win | 18.6416 |
| net_avg_loss | -34.9493 |
| avg_hold_time_bars | 4.5848 |
| exposure | 0.1529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
