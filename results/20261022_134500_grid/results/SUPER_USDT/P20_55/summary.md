# EMA Hourly Continuation — SUPER/USDT P20_55

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.5397 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8602 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -5.5871 |
| sortino_ratio | -2.4368 |
| max_drawdown | 0.9483 |
| cagr | -0.6866 |
| net_avg_win | 24.9727 |
| net_avg_loss | -40.6028 |
| avg_hold_time_bars | 5.5800 |
| exposure | 0.2410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
