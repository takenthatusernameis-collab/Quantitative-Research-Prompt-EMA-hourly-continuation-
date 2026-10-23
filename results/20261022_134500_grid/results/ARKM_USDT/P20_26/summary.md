# EMA Hourly Continuation — ARKM/USDT P20_26

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1256 |
| net_profit_factor | 0.3404 |
| net_win_rate | 0.3893 |
| gross_profit_factor | 0.7628 |
| gross_win_rate | 0.4196 |
| sharpe_ratio | -13.0566 |
| sortino_ratio | -6.6643 |
| max_drawdown | 0.9998 |
| cagr | -0.9677 |
| net_avg_win | 10.5531 |
| net_avg_loss | -19.7636 |
| avg_hold_time_bars | 1.8384 |
| exposure | 0.1050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
