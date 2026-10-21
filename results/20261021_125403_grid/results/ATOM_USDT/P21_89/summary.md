# EMA Hourly Continuation — ATOM/USDT P21_89

**Symbol:** ATOM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5177 |
| gross_profit_factor | 1.0536 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -1.3175 |
| sortino_ratio | -0.4158 |
| max_drawdown | 0.4186 |
| cagr | -0.1756 |
| net_avg_win | 65.9895 |
| net_avg_loss | -87.3882 |
| avg_hold_time_bars | 16.4678 |
| exposure | 0.3600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
