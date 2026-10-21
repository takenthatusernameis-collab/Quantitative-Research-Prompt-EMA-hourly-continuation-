# EMA Hourly Continuation — FET/USDT P20_144

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.9173 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0537 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -0.4145 |
| sortino_ratio | -0.1079 |
| max_drawdown | 0.2355 |
| cagr | -0.0524 |
| net_avg_win | 82.9563 |
| net_avg_loss | -96.1216 |
| avg_hold_time_bars | 38.1220 |
| exposure | 0.5684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
