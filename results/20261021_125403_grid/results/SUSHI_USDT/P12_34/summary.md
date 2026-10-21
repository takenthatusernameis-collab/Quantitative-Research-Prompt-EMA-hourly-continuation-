# EMA Hourly Continuation — SUSHI/USDT P12_34

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7136 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9625 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -2.8342 |
| sortino_ratio | -1.0009 |
| max_drawdown | 0.6913 |
| cagr | -0.3680 |
| net_avg_win | 57.5322 |
| net_avg_loss | -76.0161 |
| avg_hold_time_bars | 6.5572 |
| exposure | 0.1816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
