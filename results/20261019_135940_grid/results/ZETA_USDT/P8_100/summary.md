# EMA Hourly Continuation — ZETA/USDT P8_100

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.7565 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 1.0786 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -2.5742 |
| sortino_ratio | -0.8763 |
| max_drawdown | 0.7175 |
| cagr | -0.3411 |
| net_avg_win | 69.7444 |
| net_avg_loss | -90.6250 |
| avg_hold_time_bars | 26.5060 |
| exposure | 0.7017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
