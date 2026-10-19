# EMA Hourly Continuation — ENS/USDT P8_200

**Symbol:** ENS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8919 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -2.3811 |
| sortino_ratio | -0.6209 |
| max_drawdown | 0.5810 |
| cagr | -0.2552 |
| net_avg_win | 54.6554 |
| net_avg_loss | -78.2395 |
| avg_hold_time_bars | 53.3743 |
| exposure | 0.8297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
