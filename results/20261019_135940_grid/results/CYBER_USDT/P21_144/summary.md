# EMA Hourly Continuation — CYBER/USDT P21_144

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6945 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -2.4653 |
| sortino_ratio | -0.7359 |
| max_drawdown | 0.5986 |
| cagr | -0.2983 |
| net_avg_win | 60.6139 |
| net_avg_loss | -82.7773 |
| avg_hold_time_bars | 28.1256 |
| exposure | 0.5804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
