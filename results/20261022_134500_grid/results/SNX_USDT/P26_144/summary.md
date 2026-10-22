# EMA Hourly Continuation — SNX/USDT P26_144

**Symbol:** SNX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9705 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -3.4187 |
| sortino_ratio | -1.1140 |
| max_drawdown | 0.7411 |
| cagr | -0.4137 |
| net_avg_win | 56.8491 |
| net_avg_loss | -77.3722 |
| avg_hold_time_bars | 17.9851 |
| exposure | 0.4378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
