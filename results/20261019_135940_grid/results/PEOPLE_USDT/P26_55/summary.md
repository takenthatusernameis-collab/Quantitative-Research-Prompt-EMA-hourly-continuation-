# EMA Hourly Continuation — PEOPLE/USDT P26_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 877 |
| net_profit_factor | 0.4811 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.7451 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -6.3857 |
| sortino_ratio | -2.6651 |
| max_drawdown | 0.9603 |
| cagr | -0.7216 |
| net_avg_win | 22.9482 |
| net_avg_loss | -37.8457 |
| avg_hold_time_bars | 4.6374 |
| exposure | 0.1840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
