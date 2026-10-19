# EMA Hourly Continuation — TRAC/USDT P55_89

**Symbol:** TRAC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.5023 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9372 |
| gross_win_rate | 0.4836 |
| sharpe_ratio | -5.3485 |
| sortino_ratio | -1.9074 |
| max_drawdown | 0.9066 |
| cagr | -0.6073 |
| net_avg_win | 30.6318 |
| net_avg_loss | -52.9795 |
| avg_hold_time_bars | 4.1092 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
