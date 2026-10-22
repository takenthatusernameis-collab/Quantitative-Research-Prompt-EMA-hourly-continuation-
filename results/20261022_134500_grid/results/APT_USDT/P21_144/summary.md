# EMA Hourly Continuation — APT/USDT P21_144

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7128 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0473 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.9661 |
| sortino_ratio | -0.5470 |
| max_drawdown | 0.5022 |
| cagr | -0.2337 |
| net_avg_win | 60.8010 |
| net_avg_loss | -87.0461 |
| avg_hold_time_bars | 33.3223 |
| exposure | 0.5968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
