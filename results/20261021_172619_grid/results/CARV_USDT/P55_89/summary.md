# EMA Hourly Continuation — CARV/USDT P55_89

**Symbol:** CARV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.5662 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.8118 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -3.0361 |
| sortino_ratio | -0.7450 |
| max_drawdown | 0.5188 |
| cagr | -0.2902 |
| net_avg_win | 61.1289 |
| net_avg_loss | -87.5133 |
| avg_hold_time_bars | 7.3640 |
| exposure | 0.0990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
