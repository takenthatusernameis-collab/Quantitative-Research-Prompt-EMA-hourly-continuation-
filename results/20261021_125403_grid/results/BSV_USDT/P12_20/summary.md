# EMA Hourly Continuation — BSV/USDT P12_20

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6689 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0310 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -2.4206 |
| sortino_ratio | -0.6408 |
| max_drawdown | 0.5696 |
| cagr | -0.2533 |
| net_avg_win | 61.7704 |
| net_avg_loss | -93.4497 |
| avg_hold_time_bars | 5.0444 |
| exposure | 0.0775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
