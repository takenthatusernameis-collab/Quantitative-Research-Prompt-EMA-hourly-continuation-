# EMA Hourly Continuation — FLR/USDT P21_26

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1388 |
| net_profit_factor | 0.2128 |
| net_win_rate | 0.3033 |
| gross_profit_factor | 0.7136 |
| gross_win_rate | 0.3682 |
| sharpe_ratio | -18.5003 |
| sortino_ratio | -10.2825 |
| max_drawdown | 1.0000 |
| cagr | -0.9964 |
| net_avg_win | 6.4213 |
| net_avg_loss | -13.1369 |
| avg_hold_time_bars | 1.9251 |
| exposure | 0.1215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
