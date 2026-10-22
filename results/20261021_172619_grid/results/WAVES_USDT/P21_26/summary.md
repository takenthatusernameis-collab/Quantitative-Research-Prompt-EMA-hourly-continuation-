# EMA Hourly Continuation — WAVES/USDT P21_26

**Symbol:** WAVES/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 199 |
| net_profit_factor | 0.4929 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.7775 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -3.0477 |
| sortino_ratio | -0.6154 |
| max_drawdown | 0.5329 |
| cagr | -0.2483 |
| net_avg_win | 56.5169 |
| net_avg_loss | -90.9036 |
| avg_hold_time_bars | 5.2663 |
| exposure | 0.0476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
