# EMA Hourly Continuation — MANA/USDT P8_34

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.7201 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9690 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.8788 |
| sortino_ratio | -1.0902 |
| max_drawdown | 0.7200 |
| cagr | -0.3921 |
| net_avg_win | 53.6582 |
| net_avg_loss | -71.1887 |
| avg_hold_time_bars | 9.7271 |
| exposure | 0.3095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
