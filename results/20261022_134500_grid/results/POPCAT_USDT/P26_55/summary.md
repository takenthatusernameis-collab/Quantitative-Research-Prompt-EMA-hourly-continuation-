# EMA Hourly Continuation — POPCAT/USDT P26_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.5686 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -6.7339 |
| sortino_ratio | -2.9623 |
| max_drawdown | 0.9555 |
| cagr | -0.7624 |
| net_avg_win | 34.1175 |
| net_avg_loss | -46.6130 |
| avg_hold_time_bars | 4.1481 |
| exposure | 0.1849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
