# EMA Hourly Continuation — POPCAT/USDT P20_34

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.5101 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.7920 |
| gross_win_rate | 0.4115 |
| sharpe_ratio | -9.9326 |
| sortino_ratio | -4.7993 |
| max_drawdown | 0.9943 |
| cagr | -0.9073 |
| net_avg_win | 25.8805 |
| net_avg_loss | -33.4876 |
| avg_hold_time_bars | 2.8171 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
