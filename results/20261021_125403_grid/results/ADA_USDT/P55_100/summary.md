# EMA Hourly Continuation — ADA/USDT P55_100

**Symbol:** ADA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0125 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -1.4416 |
| sortino_ratio | -0.3653 |
| max_drawdown | 0.3773 |
| cagr | -0.1545 |
| net_avg_win | 61.2292 |
| net_avg_loss | -87.2507 |
| avg_hold_time_bars | 8.3097 |
| exposure | 0.1171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
