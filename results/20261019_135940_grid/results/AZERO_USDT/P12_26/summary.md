# EMA Hourly Continuation — AZERO/USDT P12_26

**Symbol:** AZERO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1222 |
| net_profit_factor | 0.3765 |
| net_win_rate | 0.4100 |
| gross_profit_factor | 0.8475 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -10.1522 |
| sortino_ratio | -4.9825 |
| max_drawdown | 0.9983 |
| cagr | -0.9184 |
| net_avg_win | 12.0328 |
| net_avg_loss | -22.2059 |
| avg_hold_time_bars | 3.6285 |
| exposure | 0.2006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
