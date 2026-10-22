# EMA Hourly Continuation — INJ/USDT P34_144

**Symbol:** INJ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5329 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.7793 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -4.0269 |
| sortino_ratio | -1.2494 |
| max_drawdown | 0.7929 |
| cagr | -0.4583 |
| net_avg_win | 40.5525 |
| net_avg_loss | -60.2766 |
| avg_hold_time_bars | 16.9300 |
| exposure | 0.3848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
