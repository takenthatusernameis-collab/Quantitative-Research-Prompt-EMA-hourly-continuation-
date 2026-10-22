# EMA Hourly Continuation — AVA/USDT P26_144

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.9385 |
| net_win_rate | 0.5419 |
| gross_profit_factor | 1.1670 |
| gross_win_rate | 0.5419 |
| sharpe_ratio | -0.3149 |
| sortino_ratio | -0.0919 |
| max_drawdown | 0.2464 |
| cagr | -0.0469 |
| net_avg_win | 78.7990 |
| net_avg_loss | -99.3066 |
| avg_hold_time_bars | 23.3350 |
| exposure | 0.4306 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
