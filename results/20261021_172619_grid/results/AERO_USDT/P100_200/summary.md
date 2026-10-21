# EMA Hourly Continuation — AERO/USDT P100_200

**Symbol:** AERO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.8303 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0027 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -0.8502 |
| sortino_ratio | -0.1827 |
| max_drawdown | 0.2019 |
| cagr | -0.0818 |
| net_avg_win | 83.5026 |
| net_avg_loss | -101.4717 |
| avg_hold_time_bars | 13.1911 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
