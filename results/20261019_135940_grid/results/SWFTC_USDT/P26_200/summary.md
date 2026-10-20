# EMA Hourly Continuation — SWFTC/USDT P26_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.5612 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8172 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -4.4252 |
| sortino_ratio | -1.3092 |
| max_drawdown | 0.8067 |
| cagr | -0.4755 |
| net_avg_win | 52.6166 |
| net_avg_loss | -71.4163 |
| avg_hold_time_bars | 25.0022 |
| exposure | 0.5125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
