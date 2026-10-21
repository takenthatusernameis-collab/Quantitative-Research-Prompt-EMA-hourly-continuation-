# EMA Hourly Continuation — BRETT/USDT P12_26

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.8896 |
| net_win_rate | 0.5304 |
| gross_profit_factor | 1.1210 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -0.7490 |
| sortino_ratio | -0.2302 |
| max_drawdown | 0.3203 |
| cagr | -0.1039 |
| net_avg_win | 81.3466 |
| net_avg_loss | -103.2721 |
| avg_hold_time_bars | 5.7874 |
| exposure | 0.1192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
