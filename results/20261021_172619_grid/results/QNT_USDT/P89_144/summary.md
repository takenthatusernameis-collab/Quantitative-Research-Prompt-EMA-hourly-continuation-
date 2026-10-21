# EMA Hourly Continuation — QNT/USDT P89_144

**Symbol:** QNT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.6643 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9632 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.2965 |
| sortino_ratio | -0.5633 |
| max_drawdown | 0.5033 |
| cagr | -0.2271 |
| net_avg_win | 66.3563 |
| net_avg_loss | -93.9421 |
| avg_hold_time_bars | 7.3652 |
| exposure | 0.0981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
