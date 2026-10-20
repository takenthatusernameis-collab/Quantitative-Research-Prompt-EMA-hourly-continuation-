# EMA Hourly Continuation — DGB/USDT P21_34

**Symbol:** DGB/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1231 |
| net_profit_factor | 0.3185 |
| net_win_rate | 0.3737 |
| gross_profit_factor | 0.7653 |
| gross_win_rate | 0.4045 |
| sharpe_ratio | -13.1319 |
| sortino_ratio | -6.5638 |
| max_drawdown | 0.9998 |
| cagr | -0.9686 |
| net_avg_win | 10.1589 |
| net_avg_loss | -19.0291 |
| avg_hold_time_bars | 2.7116 |
| exposure | 0.1517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
