# EMA Hourly Continuation — LISTA/USDT P12_144

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.9265 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0931 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -0.4481 |
| sortino_ratio | -0.1321 |
| max_drawdown | 0.2019 |
| cagr | -0.0641 |
| net_avg_win | 88.6098 |
| net_avg_loss | -104.8915 |
| avg_hold_time_bars | 32.2795 |
| exposure | 0.6156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
