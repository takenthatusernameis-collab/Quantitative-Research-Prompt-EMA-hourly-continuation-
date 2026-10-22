# EMA Hourly Continuation — TIA/USDT P34_144

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.5617 |
| sortino_ratio | -0.7592 |
| max_drawdown | 0.6058 |
| cagr | -0.3024 |
| net_avg_win | 63.4071 |
| net_avg_loss | -85.2472 |
| avg_hold_time_bars | 20.9797 |
| exposure | 0.4225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
