# EMA Hourly Continuation — STX/USDT P26_144

**Symbol:** STX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7246 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0029 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -2.0285 |
| sortino_ratio | -0.6000 |
| max_drawdown | 0.5556 |
| cagr | -0.2502 |
| net_avg_win | 60.1191 |
| net_avg_loss | -85.2317 |
| avg_hold_time_bars | 24.3498 |
| exposure | 0.4914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
