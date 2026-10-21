# EMA Hourly Continuation — COMP/USDT P26_144

**Symbol:** COMP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7807 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0223 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -1.5025 |
| sortino_ratio | -0.4384 |
| max_drawdown | 0.4494 |
| cagr | -0.1837 |
| net_avg_win | 67.3954 |
| net_avg_loss | -88.8503 |
| avg_hold_time_bars | 25.8149 |
| exposure | 0.4881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
