# EMA Hourly Continuation — POPCAT/USDT P12_26

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6514 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8332 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -3.4120 |
| sortino_ratio | -1.0900 |
| max_drawdown | 0.6699 |
| cagr | -0.3960 |
| net_avg_win | 63.9232 |
| net_avg_loss | -78.9932 |
| avg_hold_time_bars | 5.4943 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
