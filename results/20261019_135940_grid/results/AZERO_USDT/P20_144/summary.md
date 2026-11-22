# EMA Hourly Continuation — AZERO/USDT P20_144

**Symbol:** AZERO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7507 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0184 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7665 |
| sortino_ratio | -0.4775 |
| max_drawdown | 0.4824 |
| cagr | -0.2021 |
| net_avg_win | 71.8231 |
| net_avg_loss | -94.6405 |
| avg_hold_time_bars | 37.9044 |
| exposure | 0.6278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
