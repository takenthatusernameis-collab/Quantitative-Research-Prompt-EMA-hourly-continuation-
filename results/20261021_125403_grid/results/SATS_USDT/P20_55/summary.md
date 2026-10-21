# EMA Hourly Continuation — SATS/USDT P20_55

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.6347 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.8241 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -3.7371 |
| sortino_ratio | -1.2331 |
| max_drawdown | 0.7719 |
| cagr | -0.4357 |
| net_avg_win | 55.3060 |
| net_avg_loss | -68.5644 |
| avg_hold_time_bars | 8.5945 |
| exposure | 0.2120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
