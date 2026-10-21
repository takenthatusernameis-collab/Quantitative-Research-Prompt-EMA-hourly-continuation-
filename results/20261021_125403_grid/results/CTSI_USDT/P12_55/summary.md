# EMA Hourly Continuation — CTSI/USDT P12_55

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.6801 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -3.9217 |
| sortino_ratio | -1.4978 |
| max_drawdown | 0.8287 |
| cagr | -0.4986 |
| net_avg_win | 53.2069 |
| net_avg_loss | -65.4923 |
| avg_hold_time_bars | 10.4820 |
| exposure | 0.3440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
