# EMA Hourly Continuation — CVX/USDT P8_144

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6781 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9057 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.3230 |
| sortino_ratio | -0.6066 |
| max_drawdown | 0.5308 |
| cagr | -0.2558 |
| net_avg_win | 66.4750 |
| net_avg_loss | -87.4896 |
| avg_hold_time_bars | 50.2500 |
| exposure | 0.8040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
