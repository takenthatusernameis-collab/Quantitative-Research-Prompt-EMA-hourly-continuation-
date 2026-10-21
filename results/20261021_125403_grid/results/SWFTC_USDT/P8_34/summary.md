# EMA Hourly Continuation — SWFTC/USDT P8_34

**Symbol:** SWFTC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7781 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0168 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2282 |
| sortino_ratio | -0.8269 |
| max_drawdown | 0.6265 |
| cagr | -0.3158 |
| net_avg_win | 64.3263 |
| net_avg_loss | -82.6692 |
| avg_hold_time_bars | 9.0149 |
| exposure | 0.2745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
