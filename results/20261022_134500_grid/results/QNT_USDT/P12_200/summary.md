# EMA Hourly Continuation — QNT/USDT P12_200

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.7612 |
| net_win_rate | 0.5167 |
| gross_profit_factor | 1.0786 |
| gross_win_rate | 0.5187 |
| sharpe_ratio | -1.9778 |
| sortino_ratio | -0.6344 |
| max_drawdown | 0.5596 |
| cagr | -0.2573 |
| net_avg_win | 63.7696 |
| net_avg_loss | -89.5684 |
| avg_hold_time_bars | 29.7603 |
| exposure | 0.6885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
