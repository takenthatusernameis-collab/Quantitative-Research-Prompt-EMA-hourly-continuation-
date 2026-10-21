# EMA Hourly Continuation — AVAX/USDT P12_20

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.6280 |
| net_win_rate | 0.4575 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -2.5744 |
| sortino_ratio | -0.5788 |
| max_drawdown | 0.5155 |
| cagr | -0.2337 |
| net_avg_win | 72.8499 |
| net_avg_loss | -97.8180 |
| avg_hold_time_bars | 4.5830 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
