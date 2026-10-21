# EMA Hourly Continuation — OGN/USDT P21_144

**Symbol:** OGN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6385 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8103 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -2.9514 |
| sortino_ratio | -0.8057 |
| max_drawdown | 0.6295 |
| cagr | -0.3119 |
| net_avg_win | 64.9720 |
| net_avg_loss | -80.8185 |
| avg_hold_time_bars | 32.1227 |
| exposure | 0.5451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
