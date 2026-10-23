# EMA Hourly Continuation — OGN/USDT P26_144

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5512 |
| net_win_rate | 0.4162 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4374 |
| sharpe_ratio | -4.9331 |
| sortino_ratio | -1.5767 |
| max_drawdown | 0.8547 |
| cagr | -0.5284 |
| net_avg_win | 48.3241 |
| net_avg_loss | -62.4962 |
| avg_hold_time_bars | 20.7110 |
| exposure | 0.4864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
