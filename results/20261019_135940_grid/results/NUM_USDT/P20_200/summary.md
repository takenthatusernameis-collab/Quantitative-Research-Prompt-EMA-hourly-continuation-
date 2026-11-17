# EMA Hourly Continuation — NUM/USDT P20_200

**Symbol:** NUM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.5869 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.4259 |
| sharpe_ratio | -3.7132 |
| sortino_ratio | -1.0801 |
| max_drawdown | 0.7359 |
| cagr | -0.4017 |
| net_avg_win | 56.2552 |
| net_avg_loss | -70.4477 |
| avg_hold_time_bars | 31.2060 |
| exposure | 0.6128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
