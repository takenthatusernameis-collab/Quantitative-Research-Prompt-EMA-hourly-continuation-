# EMA Hourly Continuation — DUSK/USDT P26_89

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.7790 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -1.8274 |
| sortino_ratio | -0.5735 |
| max_drawdown | 0.5310 |
| cagr | -0.2328 |
| net_avg_win | 73.2185 |
| net_avg_loss | -87.9727 |
| avg_hold_time_bars | 13.3781 |
| exposure | 0.2943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
