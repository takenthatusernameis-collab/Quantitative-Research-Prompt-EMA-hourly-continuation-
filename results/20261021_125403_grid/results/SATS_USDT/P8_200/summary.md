# EMA Hourly Continuation — SATS/USDT P8_200

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.8202 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -0.8943 |
| sortino_ratio | -0.1955 |
| max_drawdown | 0.2530 |
| cagr | -0.0875 |
| net_avg_win | 81.7670 |
| net_avg_loss | -94.7495 |
| avg_hold_time_bars | 76.3263 |
| exposure | 0.8151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
