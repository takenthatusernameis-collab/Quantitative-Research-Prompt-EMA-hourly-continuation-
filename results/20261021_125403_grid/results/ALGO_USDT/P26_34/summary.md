# EMA Hourly Continuation — ALGO/USDT P26_34

**Symbol:** ALGO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 154 |
| net_profit_factor | 0.7314 |
| net_win_rate | 0.5195 |
| gross_profit_factor | 1.0684 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -1.1708 |
| sortino_ratio | -0.2098 |
| max_drawdown | 0.2421 |
| cagr | -0.0915 |
| net_avg_win | 72.8501 |
| net_avg_loss | -107.6865 |
| avg_hold_time_bars | 4.2208 |
| exposure | 0.0295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
