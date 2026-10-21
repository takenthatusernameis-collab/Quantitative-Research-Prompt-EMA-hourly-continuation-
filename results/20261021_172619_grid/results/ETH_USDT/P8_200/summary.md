# EMA Hourly Continuation — ETH/USDT P8_200

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9319 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -1.4514 |
| sortino_ratio | -0.2936 |
| max_drawdown | 0.3152 |
| cagr | -0.1266 |
| net_avg_win | 71.9450 |
| net_avg_loss | -96.4256 |
| avg_hold_time_bars | 90.4527 |
| exposure | 0.8264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
