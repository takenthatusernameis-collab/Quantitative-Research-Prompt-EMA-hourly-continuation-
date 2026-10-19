# EMA Hourly Continuation — ARB/USDT P21_26

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.1748 |
| net_win_rate | 0.3763 |
| gross_profit_factor | 0.7073 |
| gross_win_rate | 0.4181 |
| sharpe_ratio | -13.7172 |
| sortino_ratio | -6.7414 |
| max_drawdown | 0.9999 |
| cagr | -0.9730 |
| net_avg_win | 4.9041 |
| net_avg_loss | -16.9238 |
| avg_hold_time_bars | 1.8650 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
