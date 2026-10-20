# EMA Hourly Continuation — TFUEL/USDT P20_21

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1341 |
| net_profit_factor | 0.1472 |
| net_win_rate | 0.2640 |
| gross_profit_factor | 0.5984 |
| gross_win_rate | 0.3647 |
| sharpe_ratio | -19.9735 |
| sortino_ratio | -11.2863 |
| max_drawdown | 1.0000 |
| cagr | -0.9983 |
| net_avg_win | 4.8743 |
| net_avg_loss | -11.8800 |
| avg_hold_time_bars | 2.0790 |
| exposure | 0.1262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
