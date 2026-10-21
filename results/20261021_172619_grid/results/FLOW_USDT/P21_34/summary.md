# EMA Hourly Continuation — FLOW/USDT P21_34

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.4990 |
| net_win_rate | 0.4260 |
| gross_profit_factor | 0.7591 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -3.9549 |
| sortino_ratio | -1.0394 |
| max_drawdown | 0.7055 |
| cagr | -0.3798 |
| net_avg_win | 48.3196 |
| net_avg_loss | -71.8820 |
| avg_hold_time_bars | 5.2604 |
| exposure | 0.0808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
