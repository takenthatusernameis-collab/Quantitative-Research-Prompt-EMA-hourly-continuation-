# EMA Hourly Continuation — REQ/USDT P89_144

**Symbol:** REQ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.4217 |
| net_win_rate | 0.3627 |
| gross_profit_factor | 0.6524 |
| gross_win_rate | 0.3660 |
| sharpe_ratio | -5.3854 |
| sortino_ratio | -1.3532 |
| max_drawdown | 0.8117 |
| cagr | -0.4720 |
| net_avg_win | 52.4904 |
| net_avg_loss | -70.8471 |
| avg_hold_time_bars | 8.6797 |
| exposure | 0.1207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
