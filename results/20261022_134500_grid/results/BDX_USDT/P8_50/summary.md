# EMA Hourly Continuation — BDX/USDT P8_50

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1720 |
| net_profit_factor | 0.3122 |
| net_win_rate | 0.2680 |
| gross_profit_factor | 0.7203 |
| gross_win_rate | 0.3221 |
| sharpe_ratio | -21.6702 |
| sortino_ratio | -13.3897 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 9.8474 |
| net_avg_loss | -11.5486 |
| avg_hold_time_bars | 3.9238 |
| exposure | 0.3068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
