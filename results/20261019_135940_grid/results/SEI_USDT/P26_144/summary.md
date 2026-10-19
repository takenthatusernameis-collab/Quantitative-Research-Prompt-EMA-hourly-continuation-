# EMA Hourly Continuation — SEI/USDT P26_144

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7243 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 1.0128 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -2.0563 |
| sortino_ratio | -0.6020 |
| max_drawdown | 0.5320 |
| cagr | -0.2517 |
| net_avg_win | 62.9069 |
| net_avg_loss | -84.8882 |
| avg_hold_time_bars | 26.1991 |
| exposure | 0.5204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
