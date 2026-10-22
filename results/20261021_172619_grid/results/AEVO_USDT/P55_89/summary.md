# EMA Hourly Continuation — AEVO/USDT P55_89

**Symbol:** AEVO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6712 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.4231 |
| sortino_ratio | -0.6921 |
| max_drawdown | 0.5670 |
| cagr | -0.2721 |
| net_avg_win | 58.2965 |
| net_avg_loss | -80.9780 |
| avg_hold_time_bars | 5.9100 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
