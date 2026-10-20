# EMA Hourly Continuation — SUPER/USDT P89_100

**Symbol:** SUPER/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.3541 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8265 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -7.3247 |
| sortino_ratio | -2.5088 |
| max_drawdown | 0.9607 |
| cagr | -0.7231 |
| net_avg_win | 20.7283 |
| net_avg_loss | -46.3158 |
| avg_hold_time_bars | 2.2122 |
| exposure | 0.0578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
