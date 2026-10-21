# EMA Hourly Continuation — VELO/USDT P12_26

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7772 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 0.9976 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.4532 |
| sortino_ratio | -0.4099 |
| max_drawdown | 0.4041 |
| cagr | -0.1718 |
| net_avg_win | 67.4632 |
| net_avg_loss | -88.6228 |
| avg_hold_time_bars | 5.7617 |
| exposure | 0.1011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
