# EMA Hourly Continuation — ONE/USDT P50_55

**Symbol:** ONE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 93 |
| net_profit_factor | 0.6573 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -1.2786 |
| sortino_ratio | -0.1765 |
| max_drawdown | 0.2343 |
| cagr | -0.0778 |
| net_avg_win | 80.2265 |
| net_avg_loss | -109.5938 |
| avg_hold_time_bars | 4.7634 |
| exposure | 0.0201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
