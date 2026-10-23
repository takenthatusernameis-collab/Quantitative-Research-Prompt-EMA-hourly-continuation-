# EMA Hourly Continuation — MOVR/USDT P34_200

**Symbol:** MOVR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6526 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.8897 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.5423 |
| sortino_ratio | -0.7238 |
| max_drawdown | 0.6066 |
| cagr | -0.2891 |
| net_avg_win | 56.0227 |
| net_avg_loss | -77.0604 |
| avg_hold_time_bars | 26.0882 |
| exposure | 0.4838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
