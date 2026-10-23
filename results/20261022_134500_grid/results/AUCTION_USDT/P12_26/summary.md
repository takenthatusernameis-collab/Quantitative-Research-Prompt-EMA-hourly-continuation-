# EMA Hourly Continuation — AUCTION/USDT P12_26

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1266 |
| net_profit_factor | 0.4054 |
| net_win_rate | 0.4036 |
| gross_profit_factor | 0.8134 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -11.3079 |
| sortino_ratio | -5.6680 |
| max_drawdown | 0.9993 |
| cagr | -0.9443 |
| net_avg_win | 13.3333 |
| net_avg_loss | -22.2602 |
| avg_hold_time_bars | 3.9716 |
| exposure | 0.2276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
