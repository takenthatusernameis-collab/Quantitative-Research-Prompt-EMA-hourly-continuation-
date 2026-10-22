# EMA Hourly Continuation — ADA/USDT P21_34

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1124 |
| net_profit_factor | 0.3276 |
| net_win_rate | 0.4199 |
| gross_profit_factor | 0.9561 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -11.2678 |
| sortino_ratio | -5.3811 |
| max_drawdown | 0.9991 |
| cagr | -0.9389 |
| net_avg_win | 10.3128 |
| net_avg_loss | -22.7894 |
| avg_hold_time_bars | 2.4751 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
