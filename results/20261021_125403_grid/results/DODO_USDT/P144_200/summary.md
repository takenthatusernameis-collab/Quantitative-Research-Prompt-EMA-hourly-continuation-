# EMA Hourly Continuation — DODO/USDT P144_200

**Symbol:** DODO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.5507 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7368 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -2.8075 |
| sortino_ratio | -0.6128 |
| max_drawdown | 0.5133 |
| cagr | -0.2458 |
| net_avg_win | 61.1717 |
| net_avg_loss | -83.3170 |
| avg_hold_time_bars | 6.7941 |
| exposure | 0.0732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
