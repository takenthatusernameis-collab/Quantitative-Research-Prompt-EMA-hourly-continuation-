# EMA Hourly Continuation — TRX/USDT P26_144

**Symbol:** TRX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5182 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.9336 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -3.8521 |
| sortino_ratio | -1.0311 |
| max_drawdown | 0.7067 |
| cagr | -0.3766 |
| net_avg_win | 46.7110 |
| net_avg_loss | -77.9550 |
| avg_hold_time_bars | 25.4116 |
| exposure | 0.3985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
