# EMA Hourly Continuation — API3/USDT P12_26

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1350 |
| net_profit_factor | 0.4063 |
| net_win_rate | 0.4252 |
| gross_profit_factor | 0.8138 |
| gross_win_rate | 0.4452 |
| sharpe_ratio | -10.3145 |
| sortino_ratio | -5.3676 |
| max_drawdown | 0.9987 |
| cagr | -0.9292 |
| net_avg_win | 11.9071 |
| net_avg_loss | -21.6775 |
| avg_hold_time_bars | 3.7741 |
| exposure | 0.2316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
